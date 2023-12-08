from django.shortcuts import render
from django.http import HttpResponse
def amar(request):
    return HttpResponse("<h1><marquee>hi amar how are you</h1></marquee>")
# Create your views here.
