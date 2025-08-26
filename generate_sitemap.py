import requests

BLOG_URL = "https://alienapks.com"  # ganti dengan domain blog kamu
FEED_URL = f"{BLOG_URL}/feeds/posts/summary?alt=json&max-results=500"

r = requests.get(FEED_URL).json()

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for entry in r['feed']['entry']:
    link = next(l['href'] for l in entry['link'] if l['rel'] == 'alternate')
    updated = entry['updated']['$t'][:10]  # ambil format YYYY-MM-DD
    sitemap.append("  <url>")
    sitemap.append(f"    <loc>{link}</loc>")
    sitemap.append(f"    <lastmod>{updated}</lastmod>")
    sitemap.append("    <priority>0.8</priority>")
    sitemap.append("  </url>")

sitemap.append("</urlset>")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap))

print("✅ Sitemap berhasil digenerate:", BLOG_URL)
