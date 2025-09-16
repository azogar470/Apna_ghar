from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)



    def __str__(self):
        return self.name