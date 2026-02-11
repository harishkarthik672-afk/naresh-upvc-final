# Create comprehensive sitemap.xml for better SEO

sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  
  <!-- Homepage - Highest Priority -->
  <url>
    <loc>https://www.nareshupvc.in/</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- Main Product Pages - High Priority -->
  <url>
    <loc>https://www.nareshupvc.in/upvc-windows.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/pvc-doors.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  
  <!-- About & Contact Pages -->
  <url>
    <loc>https://www.nareshupvc.in/about.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/our-presence.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Other Product/Service Pages -->
  <url>
    <loc>https://www.nareshupvc.in/aluminium-fabrication.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/modular-kitchen.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/false-ceiling.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/painting.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/mosquito-nets.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/roofing-shed-work.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/ss-work.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/gallery.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
  
  <url>
    <loc>https://www.nareshupvc.in/services.html</loc>
    <lastmod>2026-02-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  
</urlset>'''

robots_content = '''# Robots.txt for Naresh UPVC - Optimized for SEO
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /*.py$
Disallow: /*.ps1$

# Sitemap location
Sitemap: https://www.nareshupvc.in/sitemap.xml

# Crawl-delay for better server performance
Crawl-delay: 1'''

# Write files
with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml")

with open('public/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)
print("Updated robots.txt")

print("\nSEO files updated successfully!")
