# Generated by Django 5.1.3 on 2024-11-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0002_alter_room_image_alter_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rooms/'),
        ),
    ]