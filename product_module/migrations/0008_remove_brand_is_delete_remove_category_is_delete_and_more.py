# Generated by Django 5.1.3 on 2024-11-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_rename_image_name_productimage_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='is_delete',
        ),
    ]