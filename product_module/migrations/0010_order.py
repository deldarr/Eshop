# Generated by Django 5.1.3 on 2024-11-14 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_alter_product_main_image_alter_productimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product')),
            ],
        ),
    ]