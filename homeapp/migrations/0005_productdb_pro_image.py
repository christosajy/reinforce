# Generated by Django 4.2.4 on 2023-10-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_productdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Pro_Image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
