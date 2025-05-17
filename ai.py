from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# Load your API key from environment variable for security
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

def generate_image(prompt: str, output_filename: str):
    """
    Generate an image from a text prompt using Gemini Imagen model and save it locally.
    """
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",  # Imagen model in Gemini API
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            image_size="1024x1024"
        )
    )

    # Extract the image bytes from the response
    for generated_image in response.generated_images:
        image_bytes = generated_image.image.image_bytes
        image = Image.open(BytesIO(image_bytes))
        image.save(output_filename)
        print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    prompt_text = "A futuristic city skyline at sunset, digital art"
    output_file = "generated_image.png"
    generate_image(prompt_text, output_file)
