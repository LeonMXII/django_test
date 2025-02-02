from django.urls import path

from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path("demo/", views.index, name="index")
]

