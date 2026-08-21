#!/usr/bin/env python3
"""Dependency-free SEO Growth R1/R2 validation for the static MercaTax site."""

from __future__ import annotations

import json
import pathlib
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
CANONICAL_ORIGIN = "https://www.mercatax.com"

PAGES = {
    "accounting-finance/index.html": f"{CANONICAL_ORIGIN}/accounting-finance/",
    "servicios-contabilidad-puerto-rico/index.html": f"{CANONICAL_ORIGIN}/servicios-contabilidad-puerto-rico/",
    "business-services/index.html": f"{CANONICAL_ORIGIN}/business-services/",
    "servicios-negocios-puerto-rico/index.html": f"{CANONICAL_ORIGIN}/servicios-negocios-puerto-rico/",
    "technology-services/index.html": f"{CANONICAL_ORIGIN}/technology-services/",
    "automatizacion-negocios-puerto-rico/index.html": f"{CANONICAL_ORIGIN}/automatizacion-negocios-puerto-rico/",
    "resources/index.html": f"{CANONICAL_ORIGIN}/resources/",
    "recursos-puerto-rico/index.html": f"{CANONICAL_ORIGIN}/recursos-puerto-rico/",
    "privacy.html": f"{CANONICAL_ORIGIN}/privacy.html",
    "terms.html": f"{CANONICAL_ORIGIN}/terms.html",
}

PAGE_LANG = {
    "accounting-finance/index.html": "en",
    "servicios-contabilidad-puerto-rico/index.html": "es-PR",
    "business-services/index.html": "en",
    "servicios-negocios-puerto-rico/index.html": "es-PR",
    "technology-services/index.html": "en",
    "automatizacion-negocios-puerto-rico/index.html": "es-PR",
    "resources/index.html": "en",
    "recursos-puerto-rico/index.html": "es-PR",
}

LANG_PAIRS = [
    (
        "accounting-finance/index.html",
        "servicios-contabilidad-puerto-rico/index.html",
        f"{CANONICAL_ORIGIN}/accounting-finance/",
        f"{CANONICAL_ORIGIN}/servicios-contabilidad-puerto-rico/",
    ),
    (
        "business-services/index.html",
        "servicios-negocios-puerto-rico/index.html",
        f"{CANONICAL_ORIGIN}/business-services/",
        f"{CANONICAL_ORIGIN}/servicios-negocios-puerto-rico/",
    ),
    (
        "technology-services/index.html",
        "automatizacion-negocios-puerto-rico/index.html",
        f"{CANONICAL_ORIGIN}/technology-services/",
        f"{CANONICAL_ORIGIN}/automatizacion-negocios-puerto-rico/",
    ),
    (
        "resources/index.html",
        "recursos-puerto-rico/index.html",
        f"{CANONICAL_ORIGIN}/resources/",
        f"{CANONICAL_ORIGIN}/recursos-puerto-rico/",
    ),
]

EXPECTED_SITEMAP = {
    f"{CANONICAL_ORIGIN}/",
    f"{CANONICAL_ORIGIN}/accounting-finance/",
    f"{CANONICAL_ORIGIN}/servicios-contabilidad-puerto-rico/",
    f"{CANONICAL_ORIGIN}/business-services/",
    f"{CANONICAL_ORIGIN}/servicios-negocios-puerto-rico/",
    f"{CANONICAL_ORIGIN}/technology-services/",
    f"{CANONICAL_ORIGIN}/automatizacion-negocios-puerto-rico/",
    f"{CANONICAL_ORIGIN}/resources/",
    f"{CANONICAL_ORIGIN}/recursos-puerto-rico/",
    f"{CANONICAL_ORIGIN}/privacy.html",
    f"{CANONICAL_ORIGIN}/terms.html",
}


class SEOParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.og = {}
        self.twitter = {}
        self.headings = []
        self.jsonld = []
        self.links = []
        self._capture = None
        self._buffer = []
        self._jsonld_active = False
        self._jsonld_buffer = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        tag = tag.lower()
        if tag == "html":
            self.html_lang = (attrs.get("lang") or "").strip()
        elif tag == "title":
            self._capture = "title"
            self._buffer = []
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._capture = tag
            self._buffer = []
        elif tag == "meta":
            name = (attrs.get("name") or "").lower()
            prop = (attrs.get("property") or "").lower()
            content = (attrs.get("content") or "").strip()
            if name == "description":
                self.description = content
            if prop.startswith("og:"):
                self.og[prop] = content
            if name.startswith("twitter:"):
                self.twitter[name] = content
        elif tag == "link":
            rel = (attrs.get("rel") or "").lower().split()
            href = (attrs.get("href") or "").strip()
            if "canonical" in rel:
                self.canonical = href
            if "alternate" in rel and attrs.get("hreflang") and href:
                self.alternates[(attrs.get("hreflang") or "").strip()] = href
        elif tag == "script" and (attrs.get("type") or "").lower() == "application/ld+json":
            self._jsonld_active = True
            self._jsonld_buffer = []
        elif tag == "a":
            href = (attrs.get("href") or "").strip()
            if href:
                self.links.append(href)

    def handle_data(self, data):
        if self._capture:
            self._buffer.append(data)
        if self._jsonld_active:
            self._jsonld_buffer.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title" and self._capture == "title":
            self.title = " ".join("".join(self._buffer).split())
            self._capture = None
            self._buffer = []
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self._capture == tag:
            text = " ".join("".join(self._buffer).split())
            self.headings.append((tag, text))
            self._capture = None
            self._buffer = []
        elif tag == "script" and self._jsonld_active:
            payload = "".join(self._jsonld_buffer).strip()
            if payload:
                self.jsonld.append(payload)
            self._jsonld_active = False
            self._jsonld_buffer = []


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)
    print(f"ERROR: {message}")


def warn(message: str, warnings: list[str]) -> None:
    warnings.append(message)
    print(f"WARN: {message}")


def local_target_exists(href: str) -> bool:
    if not href.startswith("/") or href.startswith("//"):
        return True
    path = href.split("#", 1)[0].split("?", 1)[0]
    if not path or path == "/":
        return (ROOT / "index.html").exists()
    rel = path.lstrip("/")
    target = ROOT / rel
    if path.endswith("/"):
        target = target / "index.html"
    return target.exists()


def parse_page(rel: str) -> SEOParser:
    parser = SEOParser()
    parser.feed((ROOT / rel).read_text(encoding="utf-8"))
    return parser


def validate() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    titles: dict[str, str] = {}
    parsed: dict[str, SEOParser] = {}

    print("== SEO Growth R1/R2 static validation ==")

    for rel, expected_canonical in PAGES.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing required page: {rel}", errors)
            continue
        parser = parse_page(rel)
        parsed[rel] = parser
        print(f"PAGE: {rel}")

        expected_lang = PAGE_LANG.get(rel)
        if expected_lang and parser.html_lang != expected_lang:
            fail(f"{rel}: html lang {parser.html_lang!r} != {expected_lang!r}", errors)

        if not parser.title:
            fail(f"{rel}: missing title", errors)
        elif parser.title in titles:
            fail(f"{rel}: duplicate title also used by {titles[parser.title]}", errors)
        else:
            titles[parser.title] = rel

        if not parser.description:
            fail(f"{rel}: missing meta description", errors)
        if parser.canonical != expected_canonical:
            fail(f"{rel}: canonical {parser.canonical!r} != {expected_canonical!r}", errors)

        h1s = [text for level, text in parser.headings if level == "h1"]
        if len(h1s) != 1 or not h1s[0]:
            fail(f"{rel}: expected exactly one non-empty H1, found {h1s}", errors)
        empty = [level for level, text in parser.headings if not text]
        if empty:
            fail(f"{rel}: empty semantic headings found: {empty}", errors)

        for key in ("og:title", "og:description", "og:url", "og:image"):
            if not parser.og.get(key):
                fail(f"{rel}: missing {key}", errors)
        if parser.og.get("og:url") != expected_canonical:
            fail(f"{rel}: og:url does not match canonical", errors)
        for key in ("twitter:card", "twitter:title", "twitter:description"):
            if not parser.twitter.get(key):
                fail(f"{rel}: missing {key}", errors)

        for payload in parser.jsonld:
            try:
                json.loads(payload)
            except json.JSONDecodeError as exc:
                fail(f"{rel}: invalid JSON-LD: {exc}", errors)

        for href in parser.links:
            if not local_target_exists(href):
                fail(f"{rel}: broken local link target {href}", errors)

    for en_rel, es_rel, en_url, es_url in LANG_PAIRS:
        en = parsed.get(en_rel)
        es = parsed.get(es_rel)
        if not en or not es:
            continue
        expected = {"en-US": en_url, "es-PR": es_url, "x-default": en_url}
        if en.alternates != expected:
            fail(f"{en_rel}: hreflang set mismatch actual={en.alternates}", errors)
        if es.alternates != expected:
            fail(f"{es_rel}: hreflang set mismatch actual={es.alternates}", errors)

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "User-agent: *" not in robots or "Allow: /" not in robots:
        fail("robots.txt does not allow normal crawling", errors)
    if f"Sitemap: {CANONICAL_ORIGIN}/sitemap.xml" not in robots:
        fail("robots.txt missing absolute canonical Sitemap directive", errors)

    sitemap_path = ROOT / "sitemap.xml"
    try:
        tree = ET.parse(sitemap_path)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = {el.text.strip() for el in tree.findall("sm:url/sm:loc", ns) if el.text}
    except Exception as exc:  # pragma: no cover
        fail(f"sitemap.xml parse failed: {exc}", errors)
        locs = set()

    if locs != EXPECTED_SITEMAP:
        fail(f"sitemap URL set mismatch. actual={sorted(locs)}", errors)
    if any("/index.html" in loc for loc in locs):
        fail("sitemap contains duplicate /index.html homepage URL", errors)
    if any(urlparse(loc).netloc != "www.mercatax.com" or urlparse(loc).scheme != "https" for loc in locs):
        fail("sitemap contains a non-canonical host or scheme", errors)

    if not (ROOT / "seo-pages.css").exists():
        fail("Missing shared seo-pages.css", errors)

    home = parse_page("index.html")
    home_h1 = [text for level, text in home.headings if level == "h1" and text]
    empty_home_headings = [level for level, text in home.headings if not text]
    print("== Homepage audit ==")
    print(f"title={home.title!r}")
    print(f"description_present={bool(home.description)} canonical={home.canonical!r}")
    print(f"non_empty_h1={home_h1}")
    print(f"empty_heading_count={len(empty_home_headings)}")
    if len(home_h1) != 1:
        warn("homepage does not currently expose exactly one non-empty H1", warnings)
    if empty_home_headings:
        warn(f"homepage contains {len(empty_home_headings)} empty semantic heading(s)", warnings)
    if home.canonical != f"{CANONICAL_ORIGIN}/":
        warn("homepage self-referencing canonical is missing or incorrect", warnings)

    print(f"RESULT: errors={len(errors)} warnings={len(warnings)}")
    if errors:
        return 1
    print("PASS: SEO Growth R1/R2 static validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
