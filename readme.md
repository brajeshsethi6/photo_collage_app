Here’s a sample `README.md` for your project that provides detailed descriptions of the constant variables and the overall functionality of the script:

---

# Image Collage Generator

This Python script generates collages of images from a specified folder, where each image is accompanied by its filename, and the collage is organized on an A4-sized canvas. The script supports text wrapping under the images and centers the last image(s) if the number of images is odd in the final row.

## Features

- **Collage Creation**: Automatically creates collages from images in a directory and arranges them in rows and columns.
- **Text Wrapping**: Wraps filenames after 30 characters and displays them under each image.
- **Last Row Centering**: Centers images in the last row if there is an odd number of images.
- **Customizable Output**: The collage is saved in PNG format at 300 DPI resolution on an A4-sized canvas.
  
## Constant Variables

The script utilizes several constant variables to define the collage dimensions, image spacing, margins, text properties, and more. Here is a detailed explanation of each constant:

### Canvas and DPI Constants

- **`dpi = 300`**: The dots-per-inch (DPI) resolution for the output collage image. Higher values result in higher resolution images, and 300 DPI is typical for high-quality print output.
- **`a4_width_inch = 8.27`**: The width of an A4 page in inches (standard A4 size is 8.27 x 11.69 inches).
- **`a4_height_inch = 11.69`**: The height of an A4 page in inches.
  
### Margins and Spacing

- **`page_margin_inch = 0.5`**: The margin on the edges of the A4 page in inches. This margin is applied on all sides, ensuring that the images and text do not touch the edge of the canvas.
- **`photo_margin_inch = 0.2`**: The spacing between images in inches. It defines the amount of space between two images horizontally and vertically.
- **`text_height_inch = 0.5`**: The height allocated for the text (filename) under each image, in inches.
- **`header_height_inch = 0.5`**: The height of the header area at the top of the collage where the folder name is displayed, in inches.

### Font Sizes

- **`font_size = 60`**: The font size for the filenames displayed under each image.
- **`header_font_size = 80`**: The font size for the header text at the top of the collage, typically showing the folder name.

### Image Layout

- **`collage_width`**: The total width of the collage in pixels, derived from the A4 page width and the specified DPI (`collage_width = a4_width_inch * dpi`).
- **`collage_height`**: The total height of the collage in pixels, derived from the A4 page height and the specified DPI (`collage_height = a4_height_inch * dpi`).
- **`page_margin`**: The page margin in pixels, calculated by multiplying `page_margin_inch` by the DPI (`page_margin = page_margin_inch * dpi`).
- **`photo_margin`**: The space between the images in pixels, derived from the `photo_margin_inch` value (`photo_margin = photo_margin_inch * dpi`).
- **`text_height`**: The height of the area for text (filename) in pixels (`text_height = text_height_inch * dpi`).
- **`header_height`**: The height of the header text area in pixels (`header_height = header_height_inch * dpi`).

### Text Wrapping

- **`max_text_length = 30`**: The maximum number of characters in each line of the filename before it is wrapped to the next line.

### Derived Layout Values

- **`usable_width`**: The width of the canvas that is available for placing images after accounting for the margins.
- **`usable_height`**: The height of the canvas available for placing images and text after accounting for margins, text height, and header height.

## Usage Instructions

1. **Install the Required Libraries**:
   Ensure you have `PIL` (Pillow) installed to work with images:

   ```bash
   pip install Pillow
   ```

2. **Prepare the Folders**:
   - Place all the folders with images inside a folder called `extracted_images` (you can change this path if needed).
   - Each folder in `extracted_images` should contain image files with `.png`, `.jpg`, or `.jpeg` extensions.

3. **Run the Script**:
   After setting up the folders, run the script:

   ```bash
   python collage_generator.py
   ```

4. **Collage Output**:
   The script will generate a collage for each folder of images and save it to the `collages` folder. Each collage will be named as `{folder_name}_collage.png`.

## Example File Structure

```
project_folder/
│
├── collage_generator.py
├── extracted_images/
│   ├── folder1/
│   │   ├── image1.png
│   │   ├── image2.jpg
│   │   └── ...
│   ├── folder2/
│   │   ├── image1.jpeg
│   │   ├── image2.png
│   │   └── ...
│   └── ...
└── collages/
    ├── folder1_collage.png
    ├── folder2_collage.png
    └── ...
```

## Output Format

- The output will be a high-quality PNG file (300 DPI) with images arranged in rows and columns.
- Filenames of the images are displayed underneath each image and will wrap after 30 characters.
- If the number of images is odd, the last image(s) in the last row will be centered.

## Customization

You can modify the following values in the script to customize the collage output:

- **DPI**: Increase or decrease the resolution of the output image by modifying the `dpi` variable.
- **Font Size**: Adjust the text size by modifying `font_size` and `header_font_size`.
- **Margins**: Adjust the margins and spacing by changing the `page_margin_inch`, `photo_margin_inch`, `text_height_inch`, and `header_height_inch`.