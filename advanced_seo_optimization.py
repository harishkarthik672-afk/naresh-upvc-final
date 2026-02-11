# Advanced SEO Optimization Script for Naresh UPVC
# Goal: Rank for "upvc" keyword, not just "naresh upvc"

import os
import re
from pathlib import Path

def update_html_files_seo():
    """Update all HTML files with advanced SEO optimizations"""
    
    public_dir = Path("public")
    html_files = list(public_dir.glob("*.html"))
    
    for html_file in html_files:
        print(f"\nProcessing: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Add/Update favicon references (both ICO and PNG for compatibility)
        # Remove old favicon link if exists
        content = re.sub(r'<link rel="icon"[^>]*>', '', content)
        
        # Add new favicon links after charset meta tag
        favicon_links = '''<link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon.png">'''
        
        # Insert after charset or viewport meta tag
        if '<meta charset="UTF-8">' in content:
            content = content.replace('<meta charset="UTF-8">', 
                                    f'<meta charset="UTF-8">\n    {favicon_links}')
        
        # 2. Enhance keywords for broader UPVC ranking
        # Update keywords meta tag to focus more on generic UPVC terms
        enhanced_keywords = '''<meta name="keywords" content="upvc windows, upvc doors, upvc window price, upvc windows near me, upvc door price, best upvc windows, upvc window manufacturers, upvc sliding windows, upvc casement windows, soundproof windows, energy efficient windows, waterproof doors, upvc windows Tamil Nadu, upvc windows Chennai, upvc windows Kanchipuram, Naresh UPVC, upvc fabricators, upvc dealers">'''
        
        # Replace existing keywords meta tag
        content = re.sub(r'<meta name="keywords"[^>]*>', enhanced_keywords, content)
        
        # 3. Add structured data for better search visibility
        # Check if FAQ schema exists, if not add it
        if '"@type": "FAQPage"' not in content and html_file.name == 'index.html':
            faq_schema = '''
    
    <!-- FAQ Schema for Rich Snippets -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "What is uPVC?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "uPVC (unplasticized Polyvinyl Chloride) is a durable, low-maintenance material used for windows and doors. It offers excellent insulation, soundproofing, and weather resistance."
        }
      }, {
        "@type": "Question",
        "name": "Why choose uPVC windows over traditional windows?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "uPVC windows are energy-efficient, soundproof, waterproof, termite-resistant, and require minimal maintenance. They last longer than wooden windows and provide better insulation."
        }
      }, {
        "@type": "Question",
        "name": "What is the price of uPVC windows in Tamil Nadu?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "uPVC window prices vary based on size, design, and features. Contact Naresh UPVC for a free consultation and competitive pricing for your project."
        }
      }]
    }
    </script>'''
            
            # Add before </head>
            content = content.replace('</head>', f'{faq_schema}\n</head>')
        
        # 4. Add breadcrumb schema for better navigation
        if '"@type": "BreadcrumbList"' not in content and html_file.name != 'index.html':
            page_name = html_file.stem.replace('-', ' ').title()
            breadcrumb_schema = f'''
    
    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://www.nareshupvc.in/"
      }}, {{
        "@type": "ListItem",
        "position": 2,
        "name": "{page_name}",
        "item": "https://www.nareshupvc.in/{html_file.name}"
      }}]
    }}
    </script>'''
            
            content = content.replace('</head>', f'{breadcrumb_schema}\n</head>')
        
        # 5. Add alternate language tags for better regional SEO
        if '<link rel="alternate"' not in content:
            alternate_lang = '''<link rel="alternate" hreflang="en-in" href="https://www.nareshupvc.in/">
    <link rel="alternate" hreflang="en" href="https://www.nareshupvc.in/">
    <link rel="alternate" hreflang="ta-in" href="https://www.nareshupvc.in/">'''
            
            content = content.replace('</head>', f'    {alternate_lang}\n</head>')
        
        # Only write if content changed
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated: {html_file.name}")
        else:
            print(f"  No changes needed: {html_file.name}")
    
    print("\n" + "="*60)
    print("SEO Optimization Complete!")
    print("="*60)

if __name__ == "__main__":
    update_html_files_seo()
