# Generated by Django 5.1.5 on 2025-01-24 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_image_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='c',
        ),
    ]
