# Django Image Generation Application

This Django application allows you to generate images using the Stability AI's Text-to-image generation API. It leverages Celery for parallel processing to manage asynchronous calls to the API. Follow the instructions below to set up and test the application.

# Prerequisites

1. Python 3.x installed on your system
2. Redis server installed and running locally (for Celery)
3. Stability AI API key (sign up at Stability AI to get your API key)

# Installation
1. Clone the repository to your local machine:
   
git clone <repository_url>
cd <repository_name>

2. Create a virtual environment and activate it:

python3 -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows

3. Install dependencies:

pip install -r requirements.txt

# Configuration

1. Open the myproject/settings.py file and replace the SECRET_KEY value with your Django secret key.
2. Set up Celery with Redis as the broker. In myproject/settings.py, update the following settings:

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

3. Add your Stability AI API key to image_generator/tasks.py:
   
 'Authorization': 'Bearer YOUR_API_KEY'

# Running the Application

1. Start the Django development server:
   
   python manage.py runserver

3. In a separate terminal, start the Celery worker:
   
   celery -A myproject worker -l info

# API Authentication Configuration
1. To authenticate with the Stability AI API, set your API key in the generate_image Celery task (image_generator/tasks.py).
2. Replace 'YOUR_API_KEY' with your actual Stability AI API key.

# Usage
1. Once the server is running, you can access the application at http://localhost:8000.
2. Use the provided endpoints to trigger the image generation process:

/generate_images/: Trigger the generation of images using predefined prompts.

# Testing the Application

1. To trigger the image generation process, navigate to http://127.0.0.1:8000/generate_images.
2. Check the terminal running the Celery worker for logs indicating successful image generation.
3. Open your web browser and navigate to http://127.0.0.1:8000/admin.
4. Login using the admin credentials or superuser.
5. Click on the "Generated images" link to view the generated images.
