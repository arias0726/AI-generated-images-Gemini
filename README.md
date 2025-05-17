
# AI-generated-images-Gemini

AI-generated images using the Google Gemini API.

---

## Overview

This project demonstrates how to generate AI images from text prompts using the Google Gemini API with Python. It provides a simple script to interact with the Gemini Imagen model and save generated images locally.

---

## Features

- Generate high-quality images from text prompts using Google Gemini's Imagen model.
- Easy-to-use Python script with minimal dependencies.
- Saves generated images as PNG files.

---

## Requirements

- Python 3.6 or higher
- Google Gemini API key
- Python packages:
  - `google-generativeai`
  - `Pillow`
  - `python-dotenv` (optional, for environment variable management)

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Julianhornero/AI-generated-images-Gemini.git
cd AI-generated-images-Gemini
```

2. Install required Python packages:

```
pip install google-generativeai pillow python-dotenv
```

3. Set your Google Gemini API key as an environment variable:

Create a `.env` file in the project root with the following content:

```
GEMINI_API_KEY=your_api_key_here
```

Or export it directly in your shell:

```
export GEMINI_API_KEY=your_api_key_here
```

---

## Usage

Run the script `ai.py` to generate an image from a text prompt.

Example:

```
python ai.py
```

By default, the script generates an image for the prompt defined inside the script and saves it as `generated_image.png`.

---

## Example Code Snippet

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_image(prompt: str, output_file: str):
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            image_size="1024x1024"
        )
    )
    for img in response.generated_images:
        image = Image.open(BytesIO(img.image.image_bytes))
        image.save(output_file)
        print(f"Image saved as {output_file}")

if __name__ == "__main__":
    prompt = "A futuristic city skyline at sunset, digital art"
    generate_image(prompt, "generated_image.png")
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

