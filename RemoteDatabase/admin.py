from django.contrib import admin
from .models import Packages
# Register your models here.

admin.site.register(Packages) # Imports all Packages Database into the admin site for configuration
