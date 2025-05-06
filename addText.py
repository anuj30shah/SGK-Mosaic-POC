from PIL import Image, ImageDraw, ImageFont
import textwrap

def overlay_text_on_image(image_path, title, description, box1_text, box2_text, box3_text, output_path):
    # Load the image
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Calculate the maximum width for the text (1/4 of the image width)
    max_width = image_width // 4

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the text position
    text_position = (100, 120)  # Change this position as needed
    font_size = 80  # Adjust font size as needed
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)  # Using DejaVuSans-Bold

    # Wrap the title text to fit within the max width
    title_wrapped = textwrap.fill(title, width=max_width // (font_size // 2))  # Estimate character width

    # Draw the title text onto the image
    draw.text(text_position, title_wrapped, font=font, fill="black")

    # Define the position for the boxes
    box1_position = (100, 400)
    box2_position = (250, 400)
    box3_position = (175, 440)
    box_font_size = 15  # Font size for box text
    box_font = ImageFont.truetype("DejaVuSans-Bold.ttf", box_font_size)  # Using DejaVuSans

    # Draw the first box
    box1_bbox = draw.textbbox((0, 0), box1_text, font=box_font)
    box1_rect = [box1_position[0], box1_position[1], box1_position[0] + box1_bbox[2] + 20, box1_position[1] + box1_bbox[3] + 10]
    draw.rectangle(box1_rect, fill="black")
    draw.text((box1_position[0] + 10, box1_position[1] + 5), box1_text, font=box_font, fill="white")

    # Draw the second box
    box2_bbox = draw.textbbox((0, 0), box2_text, font=box_font)
    box2_rect = [box2_position[0], box2_position[1], box2_position[0] + box2_bbox[2] + 20, box2_position[1] + box2_bbox[3] + 10]
    draw.rectangle(box2_rect, fill="black")
    draw.text((box2_position[0] + 10, box2_position[1] + 5), box2_text, font=box_font, fill="white")

    # Draw the third box
    box3_bbox = draw.textbbox((0, 0), box3_text, font=box_font)
    box3_rect = [box3_position[0], box3_position[1], box3_position[0] + box3_bbox[2] + 20, box3_position[1] + box3_bbox[3] + 10]
    draw.rectangle(box3_rect, fill="black")
    draw.text((box3_position[0] + 10, box3_position[1] + 5), box3_text, font=box_font, fill="white")


    # Define additional text position
    additional_text_position = (100, 500)
    font_size_additional = 40  # Adjust font size as needed
    font_additional = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size_additional)  # Using DejaVuSans

    # Wrap the description text to fit within the max width
    description_wrapped = textwrap.fill(description, width=max_width // (font_size_additional // 2))  # Estimate character width

    # Draw the description text onto the image
    draw.text(additional_text_position, description_wrapped, font=font_additional, fill="black")

    # Save the modified image
    image.save(output_path)


# # Load the shirt image
# shirt_image_path = "/mnt/data/image.png"
# shirt_image = Image.open(shirt_image_path)

# # Define the text and font
# text = "YOUR TEXT HERE"  # Replace with your desired text
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to a .ttf font file
# font_size = 30
# font = ImageFont.truetype(font_path, font_size)

# # Create a drawing context
# draw = ImageDraw.Draw(shirt_image)

# # Define text position and color
# text_position = (50, 50)  # Adjust as needed
# text_color = "white"

# # Add text to the image
# draw.text(text_position, text, font=font, fill=text_color)

# # Save or display the result
# output_image_path = "/mnt/data/shirt_with_text.png"
# shirt_image.save(output_image_path)
# shirt_image.show()