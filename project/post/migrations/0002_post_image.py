# Generated by Django 5.0.7 on 2024-07-15 11:46

import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.image_upload_path),
        ),
    ]
