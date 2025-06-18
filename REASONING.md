# Reasoning

This repository contains a large `README.md` with many AI agent examples. To host
these examples on a website we generate static pages from the README so they can
be served under a domain such as `cloudcurio.cc`.

## Approach
1. **Static Site Generation** – `generate_pages.py` reads `README.md`, parses
   each entry and renders individual HTML pages using `markdown`. A shared theme
   defined in `site/style.css` and `site/template.html` ensures consistent look
   and embedded menu links to the home page.
2. **Deployment** – The `Dockerfile` uses the official Caddy image to serve the
   static files in `site/`. Sample configurations for running Caddy behind an
   nginx reverse proxy and via Traefik are included (`nginx.conf`, `traefik.yml`,
   `rules.yml`). A Cloudflare Tunnel configuration (`cloudflared.yml`) provides a
   secure path to expose the site without opening public ports.
3. **Extensibility** – The generation script can be re-run whenever the README
   changes to regenerate all pages. Because the site is static, it can also be
   deployed to Cloudflare Pages or any static hosting provider.

