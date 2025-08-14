import os
from PIL import Image

input_folder = input("Enter the path to your images folder: ").strip()
output_folder = 'resized_images'
max_size = (400, 400)
output_format = 'JPEG'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png','.jpg','jpeg','.webp')):
        img_path = os.path.join(input_folder, filename)

        try:
            with Image.open(img_path)as img:
                img.thumbnail(max_size, Image.LANCZOS)

                base_name = os.path.splitext(filename)[0]
                new_file = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

                img.save(new_file, output_format)
                print(f" ✅{filename} resized to {img.size} and saved as {new_file}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n All images processed with aspect ratio preserved!")
