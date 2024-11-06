from django.contrib import admin
from .models import Package, Passenger, Airport, Flight_Ticket, Hotel, Activities, Map
# Register your models here.

admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight_Ticket)
admin.site.register(Hotel)
admin.site.register(Activities)
admin.site.register(Package)
admin.site.register(Map)