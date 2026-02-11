from PIL import Image
import os

# Load the existing favicon PNG
favicon_path = "public/favicon.png"
output_ico = "public/favicon.ico"

try:
    # Open the image
    img = Image.open(favicon_path)
    
    # Convert to RGB if necessary (ICO doesn't support RGBA well in all browsers)
    if img.mode == 'RGBA':
        # Create a white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Create multiple sizes for better compatibility
    # Standard favicon sizes: 16x16, 32x32, 48x48
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    
    # Save as ICO with multiple sizes
    img.save(output_ico, format='ICO', sizes=icon_sizes)
    
    print(f"Successfully created {output_ico} with sizes: {icon_sizes}")
    
except Exception as e:
    print(f"Error creating favicon: {e}")
