import os
import re

def fix_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match <a ... href="#" ... > ... Know [Mm]ore ... </a>
    # We use a non-greedy match for the tag and then check for Know More
    def replacer(match):
        full_tag = match.group(0)
        # Only replace if the tag contains "Know More" or "Know more" in its content
        if re.search(r'Know [Mm]ore', full_tag):
            return full_tag.replace('href="#"', 'href="about.html"')
        return full_tag

    # Regex for <a> tags
    new_content = re.sub(r'<a[^>]+href="#"[^>]*>.*?</a>', replacer, content, flags=re.DOTALL | re.IGNORECASE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

public_dir = r'c:\Users\haris\Downloads\completed client 1 project\public'
for root, dirs, files in os.walk(public_dir):
    for file in files:
        if file.endswith('.html'):
            fix_links(os.path.join(root, file))
print("Done")
