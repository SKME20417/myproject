from django.db import models
from django.utils import timezone

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Image generated for prompt: {self.prompt}"




