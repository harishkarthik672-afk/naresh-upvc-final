import os
import re

directory = r'c:\Users\haris\Downloads\completed client 1 project\public'
seo_plan_path = r'c:\Users\haris\Downloads\completed client 1 project\SEO_OPTIMIZATION_PLAN.md'

# Read SEO plan and extract titles/descriptions
seo_data = {}
with open(seo_plan_path, 'r', encoding='utf-8') as f:
    plan_content = f.read()

# Pattern for page blocks: ## NUM. **FILENAME** (Page Name)
page_blocks = re.split(r'## \d+\. \*\*([^*]+)\*\*', plan_content)
for i in range(1, len(page_blocks), 2):
    filename_raw = page_blocks[i].strip().lower()
    block_content = page_blocks[i+1]
    
    # Extract title, description, canonical
    title_match = re.search(r'### TITLE:\s+```\s+(.*?)\s+```', block_content, re.DOTALL)
    desc_match = re.search(r'### META DESCRIPTION:\s+```\s+(.*?)\s+```', block_content, re.DOTALL)
    canonical_match = re.search(r'### CANONICAL:\s+```\s+(.*?)\s+```', block_content, re.DOTALL)
    
    seo_data[filename_raw] = {
        'title': title_match.group(1).strip() if title_match else None,
        'description': desc_match.group(1).strip() if desc_match else None,
        'canonical': canonical_match.group(1).strip() if canonical_match else None
    }

# Advanced Tags Template
advanced_tags_template = '''
    <meta name="author" content="Naresh UPVC">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="IN-TN">
    <meta name="geo.placename" content="Padappai, Chennai">
    <meta name="geo.position" content="12.8717;80.0163">
    <meta name="ICBM" content="12.8717, 80.0163">
    
    <!-- Open Graph Card -->
    <meta property="og:site_name" content="Naresh UPVC">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_US">
    <meta property="og:image" content="https://www.nareshupvc.in/favicon.png">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@nareshupvc">
    <meta name="twitter:image" content="https://www.nareshupvc.in/favicon.png">
'''

def update_file(filename):
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing SEO messes to start clean if needed, or just replace carefully
    # We'll just replace carefully.
    
    data = seo_data.get(filename.lower(), {})
    title = data.get('title')
    description = data.get('description')
    canonical = data.get('canonical')
    
    if not title:
        if filename == 'index.html':
            title = "Best uPVC Windows & Doors in Tamil Nadu | Naresh UPVC"
            description = "Naresh UPVC offers premium uPVC windows, doors & modular kitchens in Tamil Nadu. 35+ years trusted expertise. Free consultation. Call now!"
            canonical = "https://www.nareshupvc.in/"
        else:
            return # Skip if no data and not index
            
    # Clean up duplicate tags we might have added
    content = re.sub(r'<!-- Advanced Suite Tags Build .*? -->.*?\n', '', content, flags=re.DOTALL)
    
    # 1. Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content, flags=re.DOTALL)
    
    # 2. Update/Add Description
    if '<meta name="description"' in content:
        content = re.sub(r'<meta name="description"\s+content=".*?">', f'<meta name="description" content="{description}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</title>', f'</title>\n    <meta name="description" content="{description}">')
        
    # 3. Update Keywords
    keywords = "uPVC, uPVC Windows, uPVC Doors, Soundproof Windows Tamil Nadu, Energy Efficient Windows Chennai, Waterproof Doors Padappai, Naresh UPVC, Tamil Nadu, Chennai, Kanchipuram, Best uPVC Windows Manufacturer"
    if '<meta name="keywords"' in content:
        content = re.sub(r'<meta name="keywords"\s+content=".*?">', f'<meta name="keywords" content="{keywords}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</title>', f'</title>\n    <meta name="keywords" content="{keywords}">')

    # 4. Update Canonical
    if '<link rel="canonical"' in content:
        content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'    <link rel="canonical" href="{canonical}">\n</head>')

    # 5. Open Graph Title & Description
    if '<meta property="og:title"' in content:
        content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'    <meta property="og:title" content="{title}">\n</head>')
        
    if '<meta property="og:description"' in content:
        content = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{description}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'    <meta property="og:description" content="{description}">\n</head>')
        
    if '<meta property="og:url"' in content:
        content = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical}">', content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'    <meta property="og:url" content="{canonical}">\n</head>')

    # 6. Inject advanced meta suite (Avoid duplication by checking one unique tag)
    if 'name="geo.region"' not in content:
        content = content.replace('</head>', advanced_tags_template + '\n</head>')

    # 7. Add Twitter Title and Description
    if 'name="twitter:title"' not in content:
        twitter_tags = f'''
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
'''
        content = content.replace('</head>', twitter_tags + '\n</head>')

    # 8. Schema Markup (LocalBusiness for all, Organization for index)
    if 'application/ld+json' not in content:
        schema = f'''
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Naresh UPVC",
      "image": "https://www.nareshupvc.in/favicon.png",
      "@id": "https://www.nareshupvc.in",
      "url": "{canonical}",
      "telephone": "+91 91719 94284",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "#1/88, Walajabad Main Road, Seapanancheri",
        "addressLocality": "Padappai",
        "addressRegion": "TN",
        "postalCode": "601301",
        "addressCountry": "IN"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 12.8717,
        "longitude": 80.0163
      }},
      "openingHoursSpecification": {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00",
        "closes": "20:00"
      }},
      "sameAs": [
        "https://www.facebook.com/nareshupvc",
        "https://www.instagram.com/nareshupvc"
      ]
    }}
    </script>
'''
        content = content.replace('</head>', schema + '\n</head>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated SEO for {filename}")

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != '404.html':
        update_file(filename)
