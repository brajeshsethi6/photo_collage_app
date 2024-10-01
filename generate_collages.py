from PIL import Image, ImageDraw, ImageFont
import os

base_folder_path = 'extracted_images'
output_folder_path = 'collages'
dpi = 300
a4_width_inch = 8.27
a4_height_inch = 11.69
page_margin_inch = 0.5
photo_margin_inch = 0.2
text_height_inch = 0.5
header_height_inch = 0.5
font_size = 60
header_font_size = 80
max_text_length = 30  # Max characters per line for text wrapping

collage_width = int(a4_width_inch * dpi)
collage_height = int(a4_height_inch * dpi)
page_margin = int(page_margin_inch * dpi)
photo_margin = int(photo_margin_inch * dpi)
text_height = int(text_height_inch * dpi)
header_height = int(header_height_inch * dpi)

usable_width = collage_width - 2 * page_margin
usable_height = collage_height - 2 * page_margin - text_height * 2 - header_height

os.makedirs(output_folder_path, exist_ok=True)

def wrap_text(text, max_length):
    """Wrap text after max_length characters."""
    lines = []
    while len(text) > max_length:
        space_pos = text.rfind(' ', 0, max_length)
        if space_pos == -1:  # No space found, force wrap
            space_pos = max_length
        lines.append(text[:space_pos])
        text = text[space_pos:].strip()
    lines.append(text)  # Add remaining text
    return lines

def load_and_resize_images(folder_path):
    images = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            images.append(img)
            filenames.append(os.path.splitext(filename)[0])
    return images, filenames

def create_collage(images, filenames, folder_name, usable_width, usable_height, page_margin, photo_margin, text_height, header_height):
    num_images = len(images)
    
    # Check if there are no images
    if num_images == 0:
        print(f'No images found in {folder_name}. Skipping collage creation.')
        return None

    # Calculate the number of columns and rows based on number of images
    cols = int((num_images ** 0.5) or 1)  # Ensure there is at least one column
    rows = (num_images + cols - 1) // cols  # Calculate the number of rows

    image_width = (usable_width - (cols - 1) * photo_margin) // cols
    image_height = (usable_height - (rows - 1) * (photo_margin + text_height)) // rows
    image_size = (image_width, image_height)

    collage = Image.new('RGB', (collage_width, collage_height), color='white')
    draw = ImageDraw.Draw(collage)

    font = ImageFont.truetype("arial.ttf", font_size)
    header_font = ImageFont.truetype("arial.ttf", header_font_size)

    header_text = folder_name
    header_bbox = draw.textbbox((0, 0), header_text, font=header_font)
    header_width = header_bbox[2] - header_bbox[0]
    header_x = (collage_width - header_width) // 2
    header_y = page_margin
    draw.text((header_x, header_y), header_text, fill='black', font=header_font)

    for i, (img, filename) in enumerate(zip(images, filenames)):
        img = img.resize(image_size)
        
        # Calculate x and y for regular images
        x = page_margin + (i % cols) * (image_size[0] + photo_margin)
        y = page_margin + header_height + (i // cols) * (image_size[1] + photo_margin + text_height)

        # Check if it's the last row and there's an odd number of images in this row
        is_last_row = i // cols == rows - 1
        remaining_images_in_last_row = num_images % cols

        if is_last_row and remaining_images_in_last_row != 0 and i >= (num_images - remaining_images_in_last_row):
            # Center the last image in the last row
            row_width = remaining_images_in_last_row * (image_size[0] + photo_margin) - photo_margin
            x = (collage_width - row_width) // 2 + (i % cols) * (image_size[0] + photo_margin)

        collage.paste(img, (x, y))

        # Wrap the text after max_text_length characters
        wrapped_text = wrap_text(filename, max_text_length)

        # Draw each line of the wrapped text
        text_y = y + image_size[1] + 5
        for line in wrapped_text:
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_x = x + (image_size[0] - text_width) // 2
            draw.text((text_x, text_y), line, fill='black', font=font)
            text_y += font_size  # Move down to draw the next line

    return collage

for folder_name in os.listdir(base_folder_path):
    folder_path = os.path.join(base_folder_path, folder_name)
    if os.path.isdir(folder_path):
        images, filenames = load_and_resize_images(folder_path)
        
        # Only create collage if there are images
        if images:
            collage = create_collage(images, filenames, folder_name, usable_width, usable_height, page_margin, photo_margin, text_height, header_height)
            if collage:
                output_path = os.path.join(output_folder_path, f'{folder_name}_collage.png')
                collage.save(output_path, dpi=(dpi, dpi))
                print(f'Collage for {folder_name} saved as {output_path}')
