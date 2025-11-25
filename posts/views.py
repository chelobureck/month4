from django.shortcuts import render, redirect
from django.http import HttpResponse

def test_view(request):
    
    return HttpResponse("This is a test view")

# Create your views here.
