---
title: "Deploy a Hugo Site on Cloudflare Workers for Free"
slug: "cloudflare-workers-hugo-deploy"
date: 2026-04-24T15:00:00+09:00
draft: false
description: "How to host a Hugo static site on Cloudflare Workers Assets at zero cost, from build to custom domain with HTTPS."
categories:
  - unei-tips
tags:
  - hugo
  - cloudflare
  - static-site
  - deploy
image: "cover.jpg"
---

Want a site on your own domain but don't want to pay monthly hosting?

If all you need is a blog or announcement page over HTTPS, skip the rental server. Build a static site with Hugo, host it on **Cloudflare Workers Assets**, and run it on your custom domain for zero yen per month.

This article walks you through the full process: building the Hugo site, deploying to Cloudflare, and wiring up a custom domain.

**What you will learn:**

- Why Cloudflare Workers Assets is a strong pick, plus how it compares to alternatives
- How to configure Hugo and write a `wrangler.toml` file
- How to publish a custom domain with HTTPS and what to watch out for

---

## Why Cloudflare Workers -- free, fast, simple

Cloudflare Workers Assets serves static files (HTML, CSS, JS, images) from servers all over the world. For a personal blog, the free plan is more than enough.

### What the free plan covers

The Workers Free plan handles **100,000 requests per day** at no charge. A personal blog pulling a few dozen visits a day won't come close to that limit. Even if each page triggers 10 requests (HTML + CSS + JS + images), you can serve up to 10,000 page views per day.

You also skip OS updates and security patches. Hugo outputs plain HTML -- no PHP or database vulnerabilities to worry about.

### How it compares to other free hosts

Several platforms host static sites for free. Here is a quick comparison.

| Feature | Cloudflare Workers | GitHub Pages | Vercel | Netlify |
|---|---|---|---|---|
| Free quota | 100,000 req/day | unlimited (fair use) | 100 GB/mo transfer | 100 GB/mo transfer |
| Custom domain | yes | yes | yes | yes |
| SSL certificate | auto | auto | auto | auto |
| Speed from Japan | good (Tokyo edge) | good | good | slower |
| Build pipeline | none (build elsewhere) | GitHub Actions | auto-build | auto-build |
| CLI deploy | `wrangler` | `git push` | `vercel` | `netlify deploy` |

Cloudflare's edge is its **300+ edge locations** worldwide. Multiple edges serve Japan, so pages load fast for your viewers.

Note that Workers Assets has no built-in build step. You build Hugo locally or via GitHub Actions, then deploy the generated `public/` directory. The next sections show you how.

---

## Setting up the Hugo build

Before deploying, make sure Hugo builds your site correctly. This guide assumes you have **Hugo (extended edition)** installed and your site files are ready.

### Check your Hugo version

Run this in your terminal:

```bash
hugo version
```

If the output says `extended`, you are good. Themes that use SCSS require the extended build. If it does not, grab the extended edition from the [Hugo releases page](https://github.com/gohugoio/hugo/releases) and reinstall.

### Update the config file

Open `hugo.toml` (or `config.toml`) and set `baseURL` to your actual domain:

```toml
baseURL = "https://vtblog.vvil.jp/"
```

A wrong `baseURL` breaks CSS and image paths, so set this after confirming the deploy URL.

### Run the build

Build the site with:

```bash
hugo --gc --minify
```

- `--gc` removes unused cache files
- `--minify` strips whitespace from HTML, CSS, and JS to shrink file sizes

On success, Hugo writes everything into a `public/` directory at the project root.

```bash
# Check what was generated
ls public/
# index.html  p/  categories/  tags/  ...
```

If the build fails, the usual culprits are a missing theme install or a typo in front matter. Follow the error message and fix accordingly.

---

## Deploying to Cloudflare

With a clean Hugo build in hand, deploy it to Cloudflare Workers Assets using the official CLI tool called Wrangler.

### Step 1: Create a Cloudflare account

Sign up at the [Cloudflare dashboard](https://dash.cloudflare.com/sign-up). You only need an email and password -- no credit card required.

### Step 2: Install Wrangler

Wrangler is the command-line tool for Workers. With Node.js installed, run:

```bash
npm install -g wrangler
```

No Node.js yet? Grab the LTS version (18 or later) from the [Node.js website](https://nodejs.org/).

### Step 3: Log in with Wrangler

```bash
wrangler login
```

A browser window opens and asks you to grant access. Click "Allow," and the terminal will confirm you are logged in.

### Step 4: Create wrangler.toml

In your project root, create `wrangler.toml`. This tells Workers which directory to deploy.

```toml
name = "vtuber-blog"
compatibility_date = "2026-04-17"

[assets]
directory = "./public"
not_found_handling = "404-page"
```

Here is what each field does:

- `name` -- the Workers project name (any alphanumeric string)
- `compatibility_date` -- runtime compatibility date; today's date works fine
- `directory` -- the folder to deploy; point this at Hugo's `./public` output
- `not_found_handling` -- returns a 404 page for unknown paths

You can also use JSON format (`wrangler.jsonc`). TOML or JSON, the behavior is the same.

### Step 5: Deploy

Build first, then deploy:

```bash
# Build
hugo --gc --minify

# Deploy
npx wrangler deploy
```

The first deploy creates a new project on Cloudflare. It finishes in seconds and gives you a URL like `https://<project-name>.<account>.workers.dev`.

```bash
# Example output
# Uploaded vtuber-blog
# Published vtuber-blog (x.xx sec)
#   https://vtuber-blog.<your-account>.workers.dev
```

Open that URL in your browser and check that the site loads. For future updates, just run `hugo --gc --minify && npx wrangler deploy` again.

---

## Custom domain setup and gotchas

The default `*.workers.dev` URL works, but a custom domain looks more professional. Here is how to set one up when your domain is managed by Cloudflare.

### Step 1: Add the domain to Cloudflare

In the Cloudflare dashboard, click "Add a site" and enter your domain. Cloudflare will ask you to change the nameservers. Update them in your registrar's control panel (e.g. Google Domains, Namecheap).

### Step 2: Attach the domain to your Worker

Go to "Workers & Pages" in the dashboard, open your project, then navigate to "Settings" then "Domains & Routes" then "Custom Domains." Add your domain there.

If the domain is already on Cloudflare, DNS records are configured for you automatically. No manual record editing needed.

### Step 3: Verify the SSL certificate

Cloudflare issues a **free SSL certificate** for custom domains automatically. It activates within minutes, and your site becomes reachable over `https://`. No need for external services like Let's Encrypt.

### DNS propagation note

After changing nameservers, propagation can take **up to 24 hours** worldwide. During that window, some regions may see the old server and others the new one. Wait about half a day before worrying.

### Domain setup checklist

- [ ] Nameservers changed to the pair Cloudflare provided
- [ ] Custom domain added in the Worker's domain settings
- [ ] `https://` shows a padlock icon in the browser
- [ ] `http://` redirects to `https://`

To enable the HTTP-to-HTTPS redirect, go to "SSL/TLS" then "Edge Certificates" in the dashboard and turn on "Always Use HTTPS."

---

## Wrap-up

- Cloudflare Workers Assets handles **100,000 requests/day** for free -- plenty for a personal blog.
- Two commands -- `hugo --gc --minify` and `npx wrangler deploy` -- push your site live in seconds.
- Custom domains with SSL are free and automatic. No server maintenance required.

Take your Hugo site (or create a fresh one with `hugo new site`), run those two commands, and you will have an `https://` URL within minutes. Zero hosting cost, zero server admin.
