from django.shortcuts import render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from pprint import pprint
# HTTPresponse
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm

def create_blog(request):
    my_blog= "Here is My Blog"
    return HttpResponse(my_blog)
