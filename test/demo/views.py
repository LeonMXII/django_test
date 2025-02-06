from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello Netology!!!")

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def api_up(request):
    return Response({"message": "API готово к работе!"})