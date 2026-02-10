import os
import re

# Directory containing HTML files
directory = r"c:\Users\haris\Downloads\completed client 1 project\public"

# Pattern to find and replacement text
pattern = r'Created by Dexaz'
replacement = r'Development by Dexaz <img src="dexaz-logo.svg" alt="Dexaz" style="height: 20px; vertical-align: middle; margin-left: 8px;"> <a href="https://www.dexaz.in/" target="_blank" class="btn-learn-more" style="margin-left: 15px; padding: 5px 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 20px; font-size: 12px; font-weight: 600; display: inline-block; transition: transform 0.3s ease;">Learn More</a>'

# Also fix the escaped HTML entities
escaped_pattern = r'Development by Dexaz &lt;img src="dexaz-logo\.svg"[^>]*&gt;[^<]*&lt;a[^>]*&gt;Learn More&lt;/a&gt;'

# Process all HTML files
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # First, fix any escaped HTML entities
        content = re.sub(escaped_pattern, replacement, content)
        
        # Then replace any remaining "Created by Dexaz" instances
        content = content.replace(pattern, replacement)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("All HTML files have been updated successfully!")
