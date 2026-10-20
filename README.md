<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img src="assets/banner-light.svg" alt="Ahmed Bebars — networks and servers, and the software that runs on them" width="100%">
</picture>

Hi, I'm Ahmed. I have worked on networks and servers in Egypt for more than twelve years, and that is still the core of what I do. On top of it I now build the software my own businesses and my clients run on: Odoo for cafés, restaurants and gyms, tools for the 3D printers I build at **DeltaFabs**, and the monitoring that tells me when any of it goes wrong before a customer does.

Almost everything I ship works in Arabic as well as English, right to left, because the people using it read Arabic first.

## Networks and servers

I run seven Ubuntu servers for my businesses and my clients — about ten Odoo instances, about twenty-five web sites, automation — behind nginx, Caddy and Traefik, and I built the tooling that looks after them.

- **Server monitoring** — a small Python agent on every server reports each minute to an n8n workflow, which also checks every site's status and certificate, and watches the routers and lines at each shop. It keeps a dashboard, sends a daily report and a daily security digest, attaches the logs to anything that trips a threshold, and alerts on Telegram and WhatsApp.
- **Cable Watch** — Egypt's internet arrives on a handful of submarine cables. A page maps every cable that lands in Egypt beside IODA's outage signals for the country and seven Egyptian ISPs, and alerts when the pattern looks like a cut rather than a local fault. Probes at each site trace the path out every fifteen minutes, so a changed route or a jump in latency on our own lines is reported too.
- **One mesh, separate clients** — every server and every site joined over Tailscale, with access rules that keep each client's machines out of reach of every other client's.
- **Printers on the network, not on a box** — point-of-sale tickets go straight from Odoo to network ESC/POS printers on port 9100, with a fallback printer when one is down, so a café keeps serving when a Raspberry Pi in the middle would have been one more thing to fail.

## Klipper and 3D printers

At DeltaFabs I build 3D printers and run them as a small farm — Voron Trident, Zero-G and machines of our own design, all on Klipper.

- **[klipper-auto-eject](https://github.com/ahmedbebars/klipper-auto-eject)** — Klipper macros that clear the bed between prints: cool down, push the parts off with a blade on the toolhead, check the bed is empty with the probe, start the next job in the queue. A web page sets it up for each printer, a farm view lists every printer on the network, and the docs come in Arabic too.
- **[FilaMind](https://github.com/filamind-app)** — I contribute to this open-source, self-hosted suite for Klipper and Moonraker: most of my commits went to **[filamind-flow](https://github.com/filamind-app/filamind-flow)**, the control panel, then to filamind-screen, filamind-3d, filamind-core and filamind-setup.

## Odoo

I sell and customise Odoo, ERP and point of sale, for cafés, restaurants and gyms in Egypt. Most of it is client work in private repositories; the public part:

- **[odoo-custom-modules](https://github.com/ahmedbebars/odoo-custom-modules)** — custom modules for calculations, inventory, planning and point of sale.
- **[filamind-iot](https://github.com/deltafabs/filamind-iot)** — a self-hosted IoT gateway addon for Odoo 19, paired with the image below.
- **[filamind-iotbox](https://github.com/deltafabs/filamind-iotbox)** — a patched Odoo IoT Box image that takes the server address on its own settings page, instead of going through Odoo's hosted pairing service.
- **[filamind-iot-proxy](https://github.com/deltafabs/filamind-iot-proxy)** — the replacement for that hosted service: pairing, certificates and a reverse tunnel, on your own machine.

Around the point of sale for my clients: direct ticket and kitchen printing, and payroll built from the attendance clock — working days, earned rest days, overtime, a reminder for a forgotten punch, and the payslip pushed to the employee's phone.

## Not on this page

Most of my software lives in private repositories, because it belongs to the businesses that run on it:

- a mobile-first, Arabic field-operations app for merchandisers and in-store promoters — check-in by location and photo, shifts, leave and daily sales, with nearly four hundred merged changes so far;
- a SaaS for sellers on Amazon.eg, .sa and .ae;
- a restaurant web site with ordering, integrated with Odoo 19;
- attendance and operations for a security-guard workforce.

Ask if that is the part you need.

## What I use

Networks and servers first: Ubuntu, Docker, nginx, Caddy, Coolify and Traefik, Cloudflare Tunnel, Tailscale, Suricata, mtr and traceroute. n8n for automation and alerting. Python for Odoo and back ends, TypeScript for web apps and PWAs, JavaScript and Klipper macros on the printers. ESC/POS printers, Raspberry Pi and Klipper/Moonraker at the hardware end. GitHub Actions for CI and releases.

## Recently pushed

<!-- pushed starts -->
- [Release v0.13.0](https://github.com/ahmedbebars/klipper-auto-eject/commit/13a9f5d16cabfc183f0aa5a0871e1cba99f69a9f) — **klipper-auto-eject**, 20 Oct
- [The parts box counter, and power switches in the farm](https://github.com/ahmedbebars/klipper-auto-eject/commit/419ee332c6a2958da2808dad80a12a6cb79a5d9a) — **klipper-auto-eject**, 20 Oct
- [Web page: the slicer lines ready to copy; farm print statistics](https://github.com/ahmedbebars/klipper-auto-eject/commit/4cc224afe41193e6f43a9609c7be815282a36b06) — **klipper-auto-eject**, 20 Oct
- [v0.12.0 docs: one-line install that asks, Arabic docs, new pictures](https://github.com/ahmedbebars/klipper-auto-eject/commit/3806bdf8f0a05311ee987a744eade2606de53551) — **klipper-auto-eject**, 20 Oct
- [Farm: the search remembers the printers you left out](https://github.com/ahmedbebars/klipper-auto-eject/commit/208558a00cfa426ee18e9243dda86728cb00f866) — **klipper-auto-eject**, 20 Oct
- [Web page: on phones the language list is a globe button, so the title fits](https://github.com/ahmedbebars/klipper-auto-eject/commit/1d498ffa00963e76bdffaaa70d139520955feca7) — **klipper-auto-eject**, 20 Oct
<!-- pushed ends -->

---

<div dir="rtl">

أنا أحمد، مهندس شبكات وسيرفرات من مصر بخبرة أكتر من ١٢ سنة. بعمل كمان سوفتوير وأودو للكافيهات والمطاعم والجيمات، وبصنّع طابعات 3D في DeltaFabs. وكل حاجة بعملها بتشتغل بالعربي، من اليمين للشمال.

</div>
