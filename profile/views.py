from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def profile_request(request):
    return render(request, 'login/views/profile.html', {})



