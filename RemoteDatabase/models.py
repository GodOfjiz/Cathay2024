from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    package_name = models.CharField(max_length=120) # Name of the package
    hotel_name = models.CharField(max_length=120) # Name of the hotel that is included in the package
    activities = models.TextField() # Name of the activities that the passenger would do
    transportation = models.TextField() # Transportation included in the packages
<<<<<<< HEAD
    passengers = models.ForeignKey(User, on_delete=models.CASCADE) # For passengers who are booking their flight and hotel
=======
    passengers = models.ForeignKey(User) # For passengers who are booking their flight and hotel
>>>>>>> main
