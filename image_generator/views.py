import logging
from django.http import JsonResponse
from .models import GeneratedImage
from .tasks import generate_image

logger = logging.getLogger(__name__)

def generate_image_view(request):
    prompts = [
        "A red flying dog",
        "A husky ninja",
        "A footballer kid",
        "A wizard on Mars",
        "Baby Dragon"
    ]
    results = []
    for prompt in prompts:
        try:
            result = generate_image.delay(prompt)
            image_data = result.get(timeout=10)
            if image_data and isinstance(image_data, dict) and 'image_url' in image_data:
                image_url = image_data['image_url']
                generated_image = GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
                results.append({'prompt': prompt, 'task_id': result.id, 'image_url': image_url})
            else:
                logger.error(f"No image URL found for prompt '{prompt}'. Task data: {image_data}")
        except TimeoutError:
            logger.error(f"Timeout occurred while processing prompt '{prompt}'")
        except Exception as e:
            logger.error(f"An error occurred for prompt '{prompt}': {str(e)}")
    return JsonResponse({'results': results})
