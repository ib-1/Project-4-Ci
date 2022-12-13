from django.db import models

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