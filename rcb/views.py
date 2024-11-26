from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def king(request):
    return HttpResponse('<h1 text-align='center''>kohli is the captain</h1>')