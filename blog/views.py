from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from pprint import pprint
# HTTPresponse
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .models import Blog
from .forms import Contact_Form


info = []
def contact(request):
    form = Contact_Form(data=request.GET or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        data={'name': name,'surname': surname,'email': email,'content': content}
        info.append(data)
        return render(request, 'contact.html', context={'info': info, 'form': form})
    return render(request, 'contact.html', context={'form':form})
def list_posts(request):
    print(request.GET)
    var1 = request.GET.get('id', None)
    posts = Blog.objects.all()
    if var1:
        posts = posts.filter(id=var1)
    context = {'posts': posts}
    return render(request, 'blog/post-list.html', context)


def create_posts(request):
    var2 = "Gönderiler burada oluşturulacak"
    return render(request, "blog/post-create.html", context={'context2': var2})


def delete_posts(request):
    var3 = "Gönderiler burada silinecek"
    return render(request, "blog/post-delete.html", context={'context3': var3})


def edit_posts(request):
    var4 = "Gönderiler burada düzenlenecek"
    return render(request, "blog/post-edit.html", context={'context4': var4})


def save_posts(request):
    var5 = "Gönderiler burada kaydelecek"
    return render(request, "blog/post-save.html", context={'context5': var5})