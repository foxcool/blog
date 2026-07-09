# darkfox.info

Personal site and blog: Hugo + PaperMod theme, bilingual (en default, ru), dark theme.
Served at https://darkfox.info and pinned to IPFS (DNSLink `_dnslink.darkfox.info`).

## Structure

- `hugo.toml` — site config (i18n, profile mode, social icons, menus)
- `content/` — markdown content; `*.ru.md` for Russian versions
- `content/posts/` — blog posts
- `themes/PaperMod` — git submodule, do not edit in place (override via `layouts/`)
- `layouts/`, `assets/` — theme overrides

## Workflow

- Local preview: `hugo server -D`
- Local prod-like sandbox: `deploy/compose.yaml` (nginx + kubo behind the local
  Traefik on the `proxy` network, domains `site-dev.darkfox.info` /
  `ipfs-dev.darkfox.info` via private DNS) — see header comment for usage
- Production build: `hugo --minify` → `public/` (gitignored)
- Deployment: Ansible role `public_website` in the infra repo clones this repo,
  builds with Hugo in Docker, serves via nginx behind Traefik, pins to IPFS
- Every page must keep canonical URL pointing to https://darkfox.info (PaperMod default) —
  critical because IPFS gateways duplicate content

## Conventions

- Content: en is default language; add `*.ru.md` alongside for Russian
- Posts as page bundles: `content/posts/<slug>/index.md` (+ `index.ru.md`, images inside)
- Commits in English, short and meaningful
