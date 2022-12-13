from django.db import models
from django.conf import settings

# Create your models here.

class room(models.Model):
    room_type = (
        ('SBD', 'SINGLE_BED'),
        ('DBD', 'DOUBLE_BED'),
        ('VIP', 'DELUXE_ROOM'),
    
    )
    number = models.IntegerField()
    catergory = models.CharField(max_length=3, choices=room_type)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.catergory} with {self.beds} beds for {self.capacity} people'

class book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} at {self.check_in} to {self.check_out}'