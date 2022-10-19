# Generated by Django 4.1.2 on 2022-10-19 15:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_restaurant_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('price', models.FloatField()),
                ('cuisine', models.PositiveSmallIntegerField(choices=[(1, 'African'), (2, 'Chinese'), (3, 'Asian'), (1, 'Irish'), (1, 'Continental')], null=True)),
                ('status', models.IntegerField(choices=[(0, 'Not Ready'), (1, 'Ready')], default=0)),
                ('cuisine_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu', to='restaurants.restaurant')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]