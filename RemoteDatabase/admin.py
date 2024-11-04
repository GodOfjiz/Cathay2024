from django.contrib import admin
from .models import Package
# Register your models here.

admin.site.register(Package) # Imports all Packages Database into the admin site for configuration
