# Generated by Django 5.0.7 on 2024-07-15 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_name_tag_tilte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tilte',
            new_name='name',
        ),
    ]
