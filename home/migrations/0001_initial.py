# Generated by Django 4.1.2 on 2022-10-31 08:54

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300, null=True)),
                ('address', models.CharField(max_length=100)),
                ('hero_image', cloudinary.models.CloudinaryField(max_length=255)),
            ],
        ),
    ]