from django.db import models

# Create your models here.
class Passenger(models.Model):
    passenger_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    budget = models.IntegerField()

class Airport(models.Model):
    airport_id = models.IntegerField()
    name = models.CharField(max_length=200)
    iso_country = models.CharField(max_length=3)
    iso_region = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    iata_code = models.CharField(max_length=4)

class Flight_Ticket(models.Model):
    ticket_id = models.IntegerField()
    passenger_name = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name="passenger_name", default=None)
    Departure = models.DateTimeField(default=None)
    Return = models.DateTimeField(default=None) # if return_date is null then the passenger is taking a one way ticket
    airport_name = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="airport_name",default="Hong Kong")
    airport_city = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="airport_city",default="Hong Kong")
    airport_iso_country = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name= "airport_iso_country",default="HK")

class Hotel(models.Model):
    Hotel_id = models.IntegerField()
    Hotel_name = models.CharField(max_length=200)
    location_country = models.CharField(max_length=200)
    location_city = models.CharField(max_length=200)

class Activities(models.Model):
    Activities_id = models.IntegerField()
    Activities_Name = models.CharField(max_length=100)
    Cost = models.IntegerField()
    Type = models.CharField(max_length=100)
    DateTime = models.DateTimeField()
    description = models.TextField()
    duration = models.IntegerField()

class Package(models.Model):
    ticket = models.ForeignKey(Flight_Ticket, on_delete=models.CASCADE) #ticket ID
    activities = models.TextField()
    locationList = models.TextField() 
    relatedServicePlatform = models.TextField() 
    packagesList = models.TextField()

class Map(models.Model):
    depature_stop = models.CharField(max_length=100)
    arrival_stop = models.CharField(max_length=100)
    duration_formatted = models.CharField(max_length=10)
    agencies = models.CharField(max_length=100)
    agencies_url = models.TextField()
    transport = models.CharField(max_length=30)