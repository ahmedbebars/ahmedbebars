"""Refresh the "Recently pushed" block in README.md.

Lists the newest commits this account wrote in public repositories,
leaving out housekeeping. Run by .github/workflows/update-readme.yml
on a schedule.
"""
import json
import os
import pathlib
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

AUTHOR = "ahmedbebars"
COUNT = 6
# messages that describe upkeep rather than a change worth showing
SKIP = ("docs:", "doc:", "chore:", "ci:", "build:", "style:", "test:", "bump ", "merge ", "wip")

README = pathlib.Path(__file__).parent / "README.md"
START, END = "<!-- pushed starts -->", "<!-- pushed ends -->"


def get(url):
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-updater",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def pushed():
    # this repository's own commits are the page, not the work on it
    query = urllib.parse.quote(f"author:{AUTHOR} is:public -repo:{AUTHOR}/{AUTHOR}")
    found = get("https://api.github.com/search/commits"
                f"?q={query}&sort=author-date&order=desc&per_page=50")
    picked, seen = [], set()
    for item in found.get("items", []):
        title = " ".join(item["commit"]["message"].splitlines()[0].split())
        key = title.lower()
        if key.startswith(SKIP) or key in seen:
            continue
        seen.add(key)
        picked.append({
            "title": title,
            "url": item["html_url"],
            "repo": item["repository"]["name"],
            "date": item["commit"]["author"]["date"],
        })
        if len(picked) == COUNT:
            break
    return picked


def escape(text):
    backslash = chr(92)
    for char in "[]":
        text = text.replace(char, backslash + char)
    return text.replace("<", "&lt;").replace(">", "&gt;")


def main():
    try:
        rows = pushed()
    except urllib.error.HTTPError as error:
        # a rate limit should leave yesterday's list standing, not fail the run
        print(f"search unavailable ({error.code}), README left as it is")
        return
    if not rows:
        print("nothing found, README left as it is")
        return

    lines = []
    for row in rows:
        day = datetime.strptime(row["date"][:10], "%Y-%m-%d").strftime("%d %b")
        lines.append(f"- [{escape(row['title'])}]({row['url']}) — **{row['repo']}**, {day}")

    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    text = README.read_text(encoding="utf-8")
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)

    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"updated {len(lines)} entries")
    else:
        print("no change")


if __name__ == "__main__":
    main()
