#!/usr/bin/env python3
"""sitemap.xml 과 feed.xml 을 다시 만듭니다.
   저장소 맨 위에서:  python3 _tools/sitemap.py
   - sitemap.xml: 공개 페이지 전부 (notes/_template.html 처럼 _ 로 시작하는 파일은 제외)
   - feed.xml: 뉴스레터·청년 브리프·현장 노트·Reading 목록에서 최근 글 30건
   lastmod 는 git 의 마지막 커밋 날짜를 씁니다.
"""
import os, re, subprocess, html
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime

SITE = "https://oje81.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KST = timezone(timedelta(hours=9))

def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cI", "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return out[:10] if out else None
    except Exception:
        return None

# ── 공개 페이지 수집 ──
pages = []
for dp, dn, fn in os.walk(ROOT):
    rel = os.path.relpath(dp, ROOT)
    parts = [] if rel == "." else rel.split(os.sep)
    if any(p.startswith((".", "_")) for p in parts):
        continue
    for f in sorted(fn):
        if not f.endswith(".html") or f.startswith("_"):
            continue
        p = os.path.normpath(os.path.join(rel, f)) if rel != "." else f
        url = SITE + "/" + p.replace(os.sep, "/")
        if url.endswith("/index.html"):
            url = url[: -len("index.html")]
        pages.append((url, p))

def prio(url):
    path = url[len(SITE):]
    if path == "/": return "1.0"
    if path.count("/") == 2 and path.endswith("/"): return "0.8"   # 목차 페이지
    return "0.6"

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, p in sorted(pages, key=lambda x: (x[0].count("/"), x[0])):
    lm = git_date(p)
    lines.append("  <url>")
    lines.append(f"    <loc>{html.escape(url)}</loc>")
    if lm: lines.append(f"    <lastmod>{lm}</lastmod>")
    lines.append(f"    <priority>{prio(url)}</priority>")
    lines.append("  </url>")
lines.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

# ── 목록에서 글 모으기 (RSS) ──
LISTS = [
    ("newsletter/index.html", "newsletter/", "국제개발봉사 브리프"),
    ("youth/index.html", "youth/", "글로벌 청년정책 브리프"),
    ("notes/index.html", "notes/", "현장 노트"),
    ("notes/reading/index.html", "notes/reading/", "Reading"),
]
item_re = re.compile(r'<li><a href="([^"]+)"><span class="no">([^<]*)</span><span class="dt">([^<]*)</span><span class="tt">(.*?)</span></a></li>', re.S)
def clean(s): return html.unescape(re.sub(r"<[^>]+>", " ", s)).strip()
def parse_date(dt):
    m = re.match(r"(\d{4})\.(\d{2})\.(\d{1,2})", dt)
    if m: return datetime(int(m[1]), int(m[2]), int(m[3]), 9, tzinfo=KST)
    m = re.match(r"(\d{4})\.(\d{2})", dt)
    if m: return datetime(int(m[1]), int(m[2]), 1, 9, tzinfo=KST)
    m = re.match(r"(\d{4})", dt)
    if m: return datetime(int(m[1]), 1, 1, 9, tzinfo=KST)
    return datetime.now(KST)

items = []
for fpath, base, series in LISTS:
    full = os.path.join(ROOT, fpath)
    if not os.path.exists(full): continue
    txt = open(full, encoding="utf-8").read()
    txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)   # 주석 안의 틀은 제외
    for href, no, dt, tt in item_re.findall(txt):
        m = re.match(r"(.*?)<span>(.*)</span>", tt, re.S)
        title, sub = (clean(m[1]), clean(m[2])) if m else (clean(tt), "")
        label = f"{series} {no}".strip()
        items.append((parse_date(dt), f"{label} · {title}", SITE + "/" + base + href, sub or series))
items.sort(key=lambda x: x[0], reverse=True)

now = datetime.now(KST)
rss = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">', "<channel>",
       "  <title>오지은 — 브리프와 기록</title>",
       f"  <link>{SITE}/</link>",
       "  <description>국제개발봉사 브리프, 글로벌 청년정책 브리프, 현장 노트, Reading</description>",
       "  <language>ko</language>",
       f"  <lastBuildDate>{format_datetime(now)}</lastBuildDate>",
       f'  <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml" />']
for d, title, link, desc in items[:30]:
    rss += ["  <item>",
            f"    <title>{html.escape(title)}</title>",
            f"    <link>{html.escape(link)}</link>",
            f"    <guid isPermaLink=\"true\">{html.escape(link)}</guid>",
            f"    <pubDate>{format_datetime(d)}</pubDate>",
            f"    <description>{html.escape(desc)}</description>",
            "  </item>"]
rss += ["</channel>", "</rss>"]
open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write("\n".join(rss) + "\n")
print(f"sitemap.xml: {len(pages)} pages / feed.xml: {len(items)} items")
