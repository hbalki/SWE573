from django.core.checks import messages
from blog.forms import Contact_Form, Blog_Form, PostQuery_Form, Comment_Form
from .models import Blog
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, reverse
from django.http import HttpResponseBadRequest
from taggit.models import Tag
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


info = []


def contact(request):
    form = Contact_Form(data=request.GET or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        data = {'name': name, 'surname': surname, 'email': email, 'content': content}
        info.append(data)
        return render(request, 'blog/contact.html', context={'info': info, 'form': form})
    return render(request, 'blog/contact.html', context={'form': form})


# def contact(request):
#     form = Contact_Form()
#     return render(request, 'blog/contact.html', context={'form': form})


def list_posts(request):
    posts = Blog.objects.all()
    page = request.GET.get('page', 1)
    form = PostQuery_Form(data=request.GET or None)
    if form.is_valid():
        search_category = form.cleaned_data.get('search_category', None)
        search = form.cleaned_data.get('search', None)
        if search:
            posts = posts.filter(Q(content__icontains=search) | Q(title__icontains=search)).distinct()
        if search_category and search_category != 'all':
            posts = posts.filter(category_choices=search_category)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {'posts': posts, 'form': form}
    return render(request, 'blog/post-list.html', context)


def detail_posts(request, slug):
    form = Comment_Form()
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/post-detail.html', context={'blog': blog, 'form': form})


def add_comment(request, slug):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    blog = get_object_or_404(Blog, slug=slug)
    form = Comment_Form(data=request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blog = blog
        new_comment.save()
        messages.success(request, 'Yorumunuz başarıyla eklendi.')
        return HttpResponseRedirect((blog.get_absolute_url()))


def create_posts(request):
    form = Blog_Form()
    if request.method == 'POST':
        form = Blog_Form(request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save()
            msg = "Tebrikler <strong> %s </strong> başlıklı gönderiniz başarıyla oluşturuldu." % blog.title
            messages.success(request, msg, extra_tags='success')
            return HttpResponseRedirect(blog.get_absolute_url())
    return render(request, 'blog/post-create.html', context={'form': form})


def delete_posts(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    msg = "<strong>{}</strong> başlıklı gönderiniz silinmiştir.".format(blog.title)
    messages.success(request, msg, extra_tags='warning')
    return HttpResponseRedirect(reverse('list'))


def edit_posts(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = Blog_Form(instance=blog, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        msg = "<strong>{}</strong> başlıklı gönderiniz güncellenmiştir.".format(blog.title)
        messages.success(request, msg, extra_tags='info')
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/post-edit.html', context=context)


def save_posts(request):
    var5 = "Gönderiler burada kaydelecek"
    return render(request, "blog/post-save.html", context={'context5': var5})


# def home_view(request):
#     common_tags = Blog.tags.most_common()[:4]
#     form = Blog_Form(request.POST)
#     if form.is_valid():
#         newpost = form.save(commit=False)
#         newpost.save()
#         form.save_m2m()
#     context = {
#         'common_tags': common_tags,
#         'form': form,
#     }
#     return render(request, 'blog/home.html', context)


# def tagged(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     common_tags = Blog.tags.most_common()[:4]
#     posts = Blog.objects.filter(tags=tag)
#     context = {
#         'tag': tag,
#         'common_tags': common_tags,
#         'posts': posts,
#     }
#     return render(request, 'blog/home.html', context)

# def index(request):
#     return render(request, 'blog/index.html', generate_preview)
# def index(request):
#     return render(request, 'blog/index.html')





# def login_request(request):
#     """ REDIRECT IF USER ALREADY LOGGED IN """
#     if request.user.is_authenticated:
#         return redirect("/posts/index")
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("/posts/index")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request, "login/login.html")
#
#
# def register_request(request):
#     if request.user.is_authenticated:
#         return redirect("/posts/index")
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("/posts/:homepage")
#         messages.error(
#             request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render(request, "login/register.html")
#
#
# def logout_request(request):
#     if not request.user.is_authenticated:
#         return redirect("/posts/index")
#
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("/posts/index")

# def generate_preview(request):
#     headers = {
#         'Access-Control-Allow-Origin': '*',
#         'Access-Control-Allow-Methods': 'GET',
#         'Access-Control-Allow-Headers': 'Content-Type',
#         'Access-Control-Max-Age': '3600',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }
#
#     url = request.get('link')
#     print(url)
#     req = requests.get(url, headers)
#     html = BeautifulSoup(req.content, 'html.parser')
#     meta_data = {
#         'title': get_title(html),
#         'description': get_description(html),
#         'image': get_image(html),
#     }
#
#     print(meta_data)
#
#     return JsonResponse(meta_data)
#
#
# def get_title(html):
#     """Scrape page title."""
#     title = None
#     if html.title.string:
#         title = html.title.string
#     elif html.find("meta", property="og:title"):
#         title = html.find("meta", property="og:title").get('content')
#     elif html.find("meta", property="twitter:title"):
#         title = html.find("meta", property="twitter:title").get('content')
#     elif html.find("h1"):
#         title = html.find("h1").string
#     return title
#
#
# def get_description(html):
#     """Scrape page description."""
#     description = None
#     if html.find("meta", property="description"):
#         description = html.find("meta", property="description").get('content')
#     elif html.find("meta", property="og:description"):
#         description = html.find(
#             "meta", property="og:description").get('content')
#     elif html.find("meta", property="twitter:description"):
#         description = html.find(
#             "meta", property="twitter:description").get('content')
#     elif html.find("p"):
#         description = html.find("p").contents
#     return description
#
#
# def get_image(html):
#     """Scrape share image."""
#     image = None
#     if html.find("meta", property="image"):
#         image = html.find("meta", property="image").get('content')
#     elif html.find("meta", property="og:image"):
#         image = html.find("meta", property="og:image").get('content')
#     elif html.find("meta", property="twitter:image"):
#         image = html.find("meta", property="twitter:image").get('content')
#     elif html.find("img", src=True):
#         image = html.find_all("img").get('src')
#     return image