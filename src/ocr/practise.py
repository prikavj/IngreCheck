import os
from google.cloud import vision

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/priyankavijeet/Desktop/Projects/IngreCheck/config/credentials.json"

def detect_text(path):
    """Detects text in the file located at the specified path."""
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with open(path, "rb") as image_file:
        content = image_file.read()

    # Create an image object from the content
    image = vision.Image(content=content)

    # Perform text detection on the image
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Print only the first detected text (entire block of text)
    if texts:
        print("Detected text:")
        # Print the first detected text block
        print(f'\n"{texts[0].description}"')

    # Handle any potential errors in the response
    if response.error.message:
        raise Exception(f"{response.error.message}\nFor more info, check: "
                        "https://cloud.google.com/apis/design/errors")

# Example usage: Replace with the actual path to your image
detect_text("/Users/priyankavijeet/Desktop/Projects/IngreCheck/data/images/image_1.jpg")
