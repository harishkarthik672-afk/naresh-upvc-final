from PIL import Image
import os
import json

def process_favicons():
    # Source is in public/favicon.png
    source_favicon = os.path.join("public", "favicon.png")
    public_dir = "public"
    
    if not os.path.exists(source_favicon):
        print(f"Error: {source_favicon} not found.")
        return

    try:
        img = Image.open(source_favicon)
        
        # Resize and save versions
        # Key is filename, Value is (width, height)
        target_sizes = {
            "android-chrome-192x192.png": (192, 192),
            "android-chrome-512x512.png": (512, 512),
            "apple-touch-icon.png": (180, 180),
            "favicon-32x32.png": (32, 32),
            "favicon-16x16.png": (16, 16)
        }
        
        for filename, size in target_sizes.items():
            # Use LANCZOS for high quality downsampling
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
    # New block including favicon.ico
    favicon_html = """
    <!-- Favicon & Mobile Icons -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#ffffff">
    """
    
    for filename in os.listdir(public_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(public_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            new_lines = []
            
            # Remove old favicon lines to avoid duplication
            # We skip lines that look like favicon links
            for line in lines:
                lower_line = line.lower()
                if 'rel="icon"' in lower_line or 'rel="apple-touch-icon"' in lower_line or 'site.webmanifest' in lower_line:
                    continue 
                # Also remove old favicon.png references if any remain as direct <link>
                if 'href="favicon.png"' in lower_line or 'href="/favicon.png"' in lower_line:
                    if '<link' in lower_line:
                         continue

                new_lines.append(line)
            
            content = "".join(new_lines)
            
            # Insert new block after <meta charset="UTF-8">
            if '<meta charset="UTF-8">' in content:
                content = content.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + favicon_html)
            elif '<head>' in content:
                content = content.replace('<head>', '<head>\n' + favicon_html)
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated headers in {filename}")

if __name__ == "__main__":
    process_favicons()
    update_html_headers()
