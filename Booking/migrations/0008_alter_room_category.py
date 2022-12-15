# Generated by Django 3.2.16 on 2022-12-15 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0007_rename_category_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('SBD', 'SINGLE BED'), ('DBD', 'DOUBLE BED'), ('VIP', 'DELUXE ROOM')], max_length=3),
        ),
    ]
