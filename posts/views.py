from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    return render(request, 'posts/views/post_list.html', {})
