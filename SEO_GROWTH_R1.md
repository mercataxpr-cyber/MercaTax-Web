# ♤ NOVA — MERCATAX SEO GROWTH R1 + R2

## Scope

Repository: `mercataxpr-cyber/MercaTax-Web`  
Branch: `nova/seo-growth-r1-20260819`  
Base SHA: `1ba3f971930225458f7bdc82f2d1b64f66dfeb82`  
Production promotion: **only after validation and hosting gate are green**

This branch preserves the current MercaTax visual identity and focuses on crawlability, canonical URLs, service architecture, bilingual Puerto Rico search discovery, internal linking, metadata, structured data, and a scalable resources foundation.

## R1 foundation

R1 established the English commercial architecture:

- `/accounting-finance/`
- `/business-services/`
- `/technology-services/`
- `/resources/`

It also added unique titles/descriptions, self-canonicals, Open Graph/Twitter metadata, semantic headings, internal links, JSON-LD, sitemap coverage, legal-page metadata, and an automated SEO gate.

The homepage semantic blockers were later closed safely without redesign: one non-empty H1, non-empty section headings, and the preferred `https://www.mercatax.com/` canonical.

## R2 — Spanish + Puerto Rico search layer

R2 adds four independent Spanish (`es-PR`) canonical routes aimed at real Puerto Rico commercial/search intent without making unverified regulated claims:

| URL | Search intent | Title | H1 |
|---|---|---|---|
| `/servicios-contabilidad-puerto-rico/` | servicios de contabilidad Puerto Rico; bookkeeping para negocios; contabilidad para pequeños y medianos negocios | `Servicios de Contabilidad para Negocios en Puerto Rico | MercaTax` | `Servicios de Contabilidad para Negocios en Puerto Rico` |
| `/servicios-negocios-puerto-rico/` | servicios para negocios Puerto Rico; sistemas y procesos de negocio | `Servicios para Negocios en Puerto Rico | MercaTax` | `Servicios y Sistemas para Negocios en Puerto Rico` |
| `/automatizacion-negocios-puerto-rico/` | automatización negocios Puerto Rico; tecnología para negocios; procesos digitales | `Automatización para Negocios en Puerto Rico | MercaTax` | `Automatización y Tecnología para Negocios en Puerto Rico` |
| `/recursos-puerto-rico/` | recursos para negocios Puerto Rico; contabilidad, operaciones y tecnología | `Recursos para Negocios en Puerto Rico | MercaTax` | `Recursos Prácticos para Negocios en Puerto Rico` |

### Bilingual architecture

Each English/Spanish pair uses reciprocal hreflang:

- `en-US`
- `es-PR`
- `x-default` → English canonical

Each page remains self-canonical. The language versions are linked visibly so users and crawlers can move between them.

### Structured data

Spanish commercial pages use only confirmed data and include:

- `Organization`
- `Service`
- `BreadcrumbList`

The Spanish resources hub includes:

- `Organization`
- `WebSite`
- `CollectionPage`
- `BreadcrumbList`

No address, phone, hours, ratings, reviews, licenses, CPA status, awards, or other real-world facts are invented.

## Sitemap

The branch sitemap contains the intended canonical public set:

- `/`
- `/accounting-finance/`
- `/servicios-contabilidad-puerto-rico/`
- `/business-services/`
- `/servicios-negocios-puerto-rico/`
- `/technology-services/`
- `/automatizacion-negocios-puerto-rico/`
- `/resources/`
- `/recursos-puerto-rico/`
- `/terms.html`
- `/privacy.html`

`/index.html` remains excluded as a duplicate homepage URL.

## Search intent and content quality

The Spanish layer reflects current Puerto Rico search-result language around accounting/bookkeeping, small and medium businesses, operating systems, and business automation. It does not copy competitor text and does not claim services MercaTax has not established publicly.

Rules:

- no mass-generated article set;
- no keyword stuffing;
- no invented tax, legal, accounting, licensing, or regulatory claims;
- regulated-content resources must be checked against current authoritative sources before publication;
- future article priorities should be informed by Search Console query/impression data.

## Technical validation

`scripts/seo_r1_validate.py` now validates the complete R1/R2 architecture:

- required files exist;
- unique titles;
- meta descriptions;
- exact self-canonicals;
- one non-empty H1 per page;
- no empty semantic headings;
- OG/Twitter metadata;
- valid JSON-LD;
- local link targets;
- exact sitemap URL set;
- canonical host/scheme;
- reciprocal English/Spanish hreflang pairs;
- `html lang` values for bilingual pages;
- homepage H1/headings/canonical audit.

## Google Search Console after production deployment

1. Confirm all new URLs return production `200` responses.
2. Re-submit `https://www.mercatax.com/sitemap.xml`.
3. Inspect and request indexing for the eight commercial/resources URLs.
4. Treat intentional host/protocol or `/index.html` redirects as canonicalization, not errors.
5. Monitor Queries, Impressions, Clicks, CTR, Average Position, indexed pages, and Core Web Vitals.
6. Use early Search Console query data to choose the first Spanish resource articles rather than publishing generic SEO content.

## Local SEO external follow-up

- complete/verify Google Business Profile with real business data;
- choose the primary category based on the actual principal service;
- confirm real phone, hours, service area, photos, and business description;
- maintain consistent NAP wherever real-world business information is published;
- request only genuine client reviews.

## Release gate

The code is eligible for production only when:

1. GitHub SEO validation passes;
2. legal readiness remains green;
3. the hosting/deployment provider can build the exact candidate successfully;
4. production URLs can be checked after release before Search Console indexing requests are made.
