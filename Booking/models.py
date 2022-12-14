from django.db import models
from django.conf import settings

# Create your models here.

class room(models.Model):
    room_type = (
        ('SBD', 'SINGLE_BED'), # what kind of room it is
        ('DBD', 'DOUBLE_BED'),
        ('VIP', 'DELUXE_ROOM'),
    
    )
    roomnumber = models.IntegerField()
    category = models.CharField(max_length=3, choices=room_type)
    beds = models.IntegerField()
    capacity = models.IntegerField() # how many people can be help within the room

    def __str__(self):
        return f'{self.roomnumber}. {self.category} with {self.beds} beds for {self.capacity} people'
        #returns a string with all the room info
        
class book(models.Model):
    # code for the variable for user and room taken from stack overflow
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    checking_in = models.DateTimeField()
    checking_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} at {self.checking_in} to {self.checking_out}'
