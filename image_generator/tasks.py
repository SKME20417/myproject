from celery import shared_task
import requests
from .models import GeneratedImage  # Import the GeneratedImage model

@shared_task
def generate_image(prompt):
    api_url = 'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'sk-zEk9iDvfEMieXkoaI7ylvGAMGvz0U5K6z00tzj5Zzl3fTJsk'  # Replace with your Stability AI API key
    }
    data = {
        'prompt': prompt,
        'num_images': 1
    }
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            image_url = response.json()['result']['images'][0]['url']
            # Save the image URL to the database
            GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
            return {'image_url': image_url}
        else:
            print(f"Failed to generate image for prompt '{prompt}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while generating image for prompt '{prompt}': {str(e)}")
    return None
