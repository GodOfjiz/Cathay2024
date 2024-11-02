from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.APIgeneration, name="API-generation"),
]
