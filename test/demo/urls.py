from django.urls import path

from . import views
from .views import home, api_up

urlpatterns = [
    path('', home, name='home'),
    path("demo/", views.index, name="index"),
    path('api/up/', api_up),
]

