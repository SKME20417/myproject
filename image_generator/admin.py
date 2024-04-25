from django.contrib import admin
from .models import GeneratedImage

@admin.register(GeneratedImage)
class GeneratedImageAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'image_url', 'created_at')  # Display these fields in the list view
    search_fields = ('prompt',)  # Allow searching by the 'prompt' field

# Register the GeneratedImageAdmin class with the GeneratedImage model
#admin.site.register(GeneratedImage, GeneratedImageAdmin)
