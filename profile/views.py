from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def my_profile_request(request):
    my_profile = "Burada benim profilim olacak"
    return HttpResponse(my_profile)

def friends_request(request):
    friends = "Burada arkadaşlarımın profili olacak"
    return render(request, "profile/profile.html")


