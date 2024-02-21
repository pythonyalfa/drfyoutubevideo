from PIL import Image


def create_thumbnail(input_path, output_path, thumbnail_size):
    # Open the image
    original_image = Image.open(input_path)

    # Resize the image to the desired thumbnail size
    thumbnail_image = original_image.resize(thumbnail_size)

    # Save the thumbnail image
    thumbnail_image.save(output_path)


# Example usage
create_thumbnail("assets/img/portfolio/schoolspirit.jpg", "assets/img/portfolio/schoolspirit.jpg", (400, 400))
