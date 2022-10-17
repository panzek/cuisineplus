# Generated by Django 4.1.2 on 2022-10-17 09:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_remove_cuisine_likes_remove_cuisine_restaurants_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuisines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('cuisine', models.PositiveSmallIntegerField(choices=[(1, 'African'), (2, 'Chinese'), (3, 'Asian'), (1, 'Irish'), (1, 'Continental')], null=True)),
                ('status', models.IntegerField(choices=[(0, 'Not Ready'), (1, 'Ready')], default=0)),
                ('cuisine_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='cuisine_likes', to=settings.AUTH_USER_MODEL)),
                ('restaurants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_cuisines', to='restaurants.restaurant')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
    ]
