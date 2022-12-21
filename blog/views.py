from django.core.checks import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, reverse
from blog.forms import Contact_Form, Blog_Form, PostQuery_Form, Comment_Form
from .models import Blog
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, reverse
from django.http import HttpResponseBadRequest
from taggit.models import Tag
from django.template.defaultfilters import slugify



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
    form = PostQuery_Form(data=request.GET or None)
    if form.is_valid():
        search_category = form.cleaned_data.get('search_category', None)
        search = form.cleaned_data.get('search', None)
        if search:
            posts = posts.filter(Q(content__icontains=search) | Q(title__icontains=search)).distinct()
        if search_category and search_category != 'all':
            posts = posts.filter(category_choices__icontains=search_category)

    context = {'posts': posts, 'form': form}
    return render(request, 'blog/post-list.html', context)


def detail_posts(request, pk):
    form = Comment_Form()
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post-detail.html', context={'blog': blog, 'form': form})


def add_comment(request, pk):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    blog = get_object_or_404(Blog, pk=pk)
    print(blog, "selam")
    # print(request.POST)
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
            # url = reverse('detail', kwargs={'pk': blog.pk})
            return HttpResponseRedirect(blog.get_absolute_url())
    return render(request, 'blog/post-create.html', context={'form': form})


def delete_posts(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponseRedirect(reverse('list'))


def edit_posts(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = Blog_Form(instance=blog, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/post-edit.html', context=context)


def save_posts(request):
    var5 = "Gönderiler burada kaydelecek"
    return render(request, "blog/post-save.html", context={'context5': var5})


def index(request):
    return render(request, 'blog/index.html')


def generate_preview(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    url = request.GET.get('link')
    print(url)
    req = requests.get(url, headers)
    html = BeautifulSoup(req.content, 'html.parser')
    meta_data = {
        'title': get_title(html),
        'description': get_description(html),
        'image': get_image(html),
    }

    print(meta_data)

    return JsonResponse(meta_data)


def get_title(html):
    """Scrape page title."""
    title = "title"
    if html.title.string:
        title = html.title.string
    elif html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    elif html.find("meta", property="twitter:title"):
        title = html.find("meta", property="twitter:title").get('content')
    elif html.find("h1"):
        title = html.find("h1").string
    return title


def get_description(html):
    """Scrape page description."""
    description = "description"
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find(
            "meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find(
            "meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description


def get_image(html):
    """Scrape share image."""
    image = "image"
    if html.find("meta", property="image"):
        image = html.find("meta", property="image").get('content')
    elif html.find("meta", property="og:image"):
        image = html.find("meta", property="og:image").get('content')
    elif html.find("meta", property="twitter:image"):
        image = html.find("meta", property="twitter:image").get('content')
    elif html.find("img", src=True):
        image = html.find_all("img").get('src')
    return image


def home_view(request):
    posts = Blog.objects.all()
    common_tags = Blog.tags.most_common()[:4]
    form = Blog_Form(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()
    context = {
        'posts': posts,
        'common_tags': common_tags,
        'form': form,
    }
    return render(request, 'home.html', context)


def detail_view(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Blog.tags.most_common()[:4]
    posts = Blog.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'posts': posts,
    }
    return render(request, 'home.html', context)
