# Generated by Django 3.2.25 on 2024-04-24 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatedimage',
            old_name='prompt_text',
            new_name='prompt',
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
