# Generated by Django 5.1 on 2024-10-07 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_health_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritionfacts',
            name='serving_size',
        ),
    ]
