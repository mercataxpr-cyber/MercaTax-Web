# ♤ NOVA — MERCATAX SEO GROWTH R1

## Scope

Repository: `mercataxpr-cyber/MercaTax-Web`  
Branch: `nova/seo-growth-r1-20260819`  
Base SHA: `1ba3f971930225458f7bdc82f2d1b64f66dfeb82`  
Production deployment: **NOT AUTHORIZED**

This R1 preserves the current MercaTax visual identity and focuses on crawlability, canonical URLs, service architecture, internal linking, metadata, structured data, and a scalable resources foundation.

## Initial audit

### Already implemented / valid

- `robots.txt` already allows crawling and references the absolute canonical sitemap URL: `https://www.mercatax.com/sitemap.xml`.
- The sitemap already used the preferred `https://www.mercatax.com/` homepage URL and no longer listed `/index.html` as a second homepage.
- `privacy.html` and `terms.html` already existed, contained substantial visible content, had one visible H1 each, and were cross-linked.
- The site already had responsive viewport metadata and a stable visual identity.

### Gaps addressed in this branch

- No dedicated crawlable landing pages existed for the three confirmed public service pillars: Accounting & Finance, Business, and Technology.
- There was no scalable `/resources/` content hub.
- Legal pages lacked self-referencing canonical tags and social metadata.
- The sitemap did not include service/category landing pages because those routes did not yet exist.
- The new service pages needed unique titles, descriptions, canonicals, social metadata, semantic headings, internal links, and structured data.

### Risk-controlled hold

The current root `index.html` is a large generated/static artifact. The connected repository interface did not expose a safe complete editable representation suitable for replacing that file without risking the approved homepage design or functionality. Because this R1 explicitly prohibits unnecessary redesign/regression, the homepage semantic rewrite is **not forced in this branch**.

Pending homepage items for a later safe edit:

- verify/add a single descriptive H1;
- normalize H2/H3 hierarchy and remove empty headings;
- verify/add self-canonical;
- verify/complete Open Graph and Twitter metadata;
- add Organization/WebSite structured data if not already present in the complete source;
- add contextual links from the homepage to the new service and resources routes;
- preserve the existing visual design exactly.

## SEO / Content Map

| URL | Purpose / intent | Query theme (conceptual, not search-volume validated) | Title | H1 | Primary CTA |
|---|---|---|---|---|---|
| `/` | Brand + multi-service discovery | MercaTax Puerto Rico; accounting business technology Puerto Rico | Existing title retained in R1; later safe target: `MercaTax | Accounting, Business & Technology in Puerto Rico` | Pending safe homepage source edit | Existing homepage CTA |
| `/accounting-finance/` | Commercial service discovery | accounting support Puerto Rico; accounting services Puerto Rico; financial organization Puerto Rico | `Accounting & Finance Support in Puerto Rico | MercaTax` | `Accounting & Finance Support for Puerto Rico Businesses` | Talk with MercaTax |
| `/business-services/` | Commercial service discovery | business services Puerto Rico; business operations Puerto Rico; business systems Puerto Rico | `Business Services in Puerto Rico | MercaTax` | `Practical Business Support in Puerto Rico` | Talk with MercaTax |
| `/technology-services/` | Commercial service discovery | technology solutions Puerto Rico; business automation Puerto Rico; digital tools Puerto Rico | `Business Technology & Automation in Puerto Rico | MercaTax` | `Technology & Automation for Puerto Rico Businesses` | Talk with MercaTax |
| `/resources/` | Informational discovery hub | Puerto Rico business resources; accounting operations technology resources | `Business Resources for Puerto Rico | MercaTax` | `Practical Resources for Puerto Rico Businesses` | Contact MercaTax / explore services |
| `/privacy.html` | Legal / trust | privacy policy MercaTax | `Política de Privacidad | MercaTax` | `Política de Privacidad` | Return to site |
| `/terms.html` | Legal / trust | terms MercaTax | `Términos y Condiciones | MercaTax` | `Términos y Condiciones` | Return to site |

## Technical SEO implemented

### Canonical and social metadata

New service/resources pages include:

- unique `<title>`;
- unique meta description;
- self-referencing canonical;
- Open Graph title, description, URL, site name, image;
- Twitter card title, description, and image;
- responsive viewport.

Legal pages now include self-referencing canonicals plus Open Graph/Twitter metadata.

### Structured data

New service pages include:

- `Organization`;
- `Service`;
- `BreadcrumbList`.

The resources hub includes:

- `Organization`;
- `WebSite`;
- `CollectionPage`;
- `BreadcrumbList`.

Only confirmed information is used. No address, phone, hours, ratings, reviews, awards, or social profiles were invented.

### Sitemap

The branch sitemap now lists only intended canonical public URLs:

- `/`
- `/accounting-finance/`
- `/business-services/`
- `/technology-services/`
- `/resources/`
- `/terms.html`
- `/privacy.html`

No `/index.html` duplicate is listed.

### Internal linking

Each new commercial page links to the other service pillars, resources, and homepage. The resources hub links back to all three service pillars. Legal pages remain reachable and cross-linked.

## Content quality rules

- No mass-generated article set was created.
- No invented tax, legal, accounting, or regulatory claims were published.
- The resources hub explicitly requires future regulated-content articles to be checked against current authoritative sources and professional review when needed.
- Keyword themes in this document are conceptual targeting directions, not claims of measured search volume.

## Local SEO

Implemented on-site:

- natural Puerto Rico relevance in titles, headings, copy, and `areaServed` structured data on new service pages;
- no location stuffing;
- no invented NAP data.

External follow-up required:

- verify/complete Google Business Profile using real business data;
- choose the primary Business Profile category based on the actual principal service, not SEO preference;
- confirm real phone, hours, service area, photos, and business description;
- keep NAP data consistent wherever published;
- request only genuine client reviews.

## Search Console follow-up after approved merge/deployment

1. Re-submit `https://www.mercatax.com/sitemap.xml`.
2. Inspect the homepage and each new canonical service/resources URL.
3. Request indexing for the new public pages after they return production `200` responses.
4. Monitor Queries, Impressions, Clicks, CTR, and Average Position.
5. Treat intentional protocol/host redirects as expected canonicalization; do not mark them fixed unless the redirect behavior is actually changed or incorrect.
6. Recheck `privacy.html` and `terms.html` only after deployment and recrawl; they are low commercial-priority URLs.

## Performance / mobile

The new pages use one small shared stylesheet, native HTML, no client-side framework, no analytics library, no webfont dependency, and no large hero image. They include responsive breakpoints, flexible grids, visible focus states, and mobile-width CTAs.

Production Core Web Vitals must still be measured after preview/deployment because field metrics cannot be certified from repository source alone.

## Pending / external

- Safe homepage semantic/metadata edit once a complete editable source representation is available.
- Production redirect verification for `/index.html` → `/` and host/protocol canonicalization should be performed against the deployed environment.
- Google Search Console submission/index requests after approved production deployment.
- Google Business Profile work with confirmed real-world business information.
- Search-demand research using Search Console query data after the new pages begin receiving impressions.
- Field Core Web Vitals and real mobile performance measurement after deployment.

## Release rule

This branch is a **preview/review candidate only**. Do not merge or deploy to production without explicit TEKI authorization.
