from PIL import Image
import os
import json

def process_favicons():
    source_favicon = "public/favicon.png"
    public_dir = "public"
    
    if not os.path.exists(source_favicon):
        print(f"Error: {source_favicon} not found.")
        return

    try:
        img = Image.open(source_favicon)
        
        # Resize and save versions
        sizes = {
            "android-chrome-192x192.png": (192, 192),
            "android-chrome-512x512.png": (512, 512),
            "apple-touch-icon.png": (180, 180),
            "favicon-32x32.png": (32, 32),
            "favicon-16x16.png": (16, 16)
        }
        
        for filename, size in sizes.items():
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            output_path = os.path.join(public_dir, filename)
            resized_img.save(output_path)
            print(f"Created {filename}")

        # Create site.webmanifest
        manifest_content = {
            "name": "Naresh UPVC",
            "short_name": "Naresh UPVC",
            "icons": [
                {
                    "src": "/android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png"
                },
                {
                    "src": "/android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png"
                }
            ],
            "theme_color": "#ffffff",
            "background_color": "#ffffff",
            "display": "standalone"
        }
        
        with open(os.path.join(public_dir, "site.webmanifest"), "w") as f:
            json.dump(manifest_content, f, indent=2)
        print("Created site.webmanifest")
            
    except Exception as e:
        print(f"Error processing favicons: {e}")

def update_html_headers():
    public_dir = "public"
    favicon_html = """
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    """
    
    for filename in os.listdir(public_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(public_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove existing heavy favicon links to avoid duplication/conflicts
            lines = content.splitlines()
            new_lines = []
            fav_inserted = False
            
            # Simple heuristic: insert after <meta charset> or <head>
            # And enable removal of old favicon lines
            
            for line in lines:
                if 'rel="icon"' in line or 'rel="apple-touch-icon"' in line or 'favico' in line:
                    continue # Skip old lines
                
                new_lines.append(line)
                
                if '<head>' in line and not fav_inserted:
                     # Wait for charset... actually let's just insert after <head> or somewhat early
                     pass
            
            # Reconstruct and insert new block nicely
            final_content = "\n".join(new_lines)
            
            # Insert new block after <meta charset="UTF-8">
            if '<meta charset="UTF-8">' in final_content:
                final_content = final_content.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">' + favicon_html)
            elif '<head>' in final_content:
                final_content = final_content.replace('<head>', '<head>' + favicon_html)
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_content)
            print(f"Updated headers in {filename}")

if __name__ == "__main__":
    process_favicons()
    update_html_headers()
