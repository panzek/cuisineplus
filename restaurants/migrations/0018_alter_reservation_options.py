# Generated by Django 4.1.2 on 2022-11-01 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0017_reservation_created_on_reservation_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-created_on']},
        ),
    ]