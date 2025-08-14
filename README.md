# 🖼️ Image Resizer Tool

## 📌 Overview
This Python script resizes and converts all images in a given folder while **preserving aspect ratio**.  
It uses the [Pillow](https://pillow.readthedocs.io/en/stable/) library to process images in bulk and save them to a separate output folder.

---

## 🚀 Features
- Resize all images in a folder at once.
- Preserve aspect ratio (no stretching or distortion).
- Convert images to a chosen format (JPEG, PNG, WEBP, etc.).
- Automatically creates the output folder if it doesn’t exist.
- Supports `.jpg`, `.jpeg`, `.png`, `.webp`.

---

## 🛠️ Requirements
- Python 3
- Pillow library

Install Pillow:
    pip install pillow

🖼️ Example

Before:
    images/cat.png → 3000×2000 pixels

After:
    resized_images/cat.jpeg → 800×533 pixels (aspect ratio preserved)

How It works:
1. Give File path and the enter
2. It automatically creates u a resized_folder and saves the images to that folder
   EXTRA
   1. If u want to resize the image size change the max_size options according to your choice
   2. instead of using enter path in imput_folder you can use 'input_folder = 'folderName''



