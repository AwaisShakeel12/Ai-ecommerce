# Generated by Django 5.1 on 2024-10-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile_images/avatar.jpg', null=True, upload_to='profile_images'),
        ),
    ]
