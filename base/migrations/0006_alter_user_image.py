# Generated by Django 5.0.3 on 2024-07-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='profile_images'),
        ),
    ]