# Generated by Django 3.2.16 on 2022-12-13 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='catergory',
            field=models.CharField(choices=[('SBD', 'SINGLE_BED'), ('DBD', 'DOUBLE_BED'), ('VIP', 'DELUXE_ROOM')], max_length=3),
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
