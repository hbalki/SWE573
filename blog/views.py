from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, reverse

from .forms import Contact_Form, Blog_Form
# HTTP response
# Create your views here.
from .models import Blog

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
    # print(reverse('create'))
    print(request.GET)
    var1 = request.GET.get('id', None)
    posts = Blog.objects.all()
    if var1:
        posts = posts.filter(id=var1)
    context = {'posts': posts}
    return render(request, 'blog/post-list.html', context)


def detail_posts(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    # blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/post-detail.html', context={'blog': blog})


def create_posts(request):
    form = Blog_Form()
    if request.method == 'POST':
        form = Blog_Form(request.POST)
        if form.is_valid():
            blog = form.save()
            # url = reverse('detail', kwargs={'pk': blog.pk})
            return HttpResponseRedirect(blog.get_absolute_url())
    return render(request, 'blog/post-create.html', context={'form': form})


def delete_posts(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponseRedirect(reverse('list'))


def edit_posts(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = Blog_Form(instance=blog, data=request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/post-edit.html', context=context)



def save_posts(request):
    var5 = "Gönderiler burada kaydelecek"
    return render(request, "blog/post-save.html", context={'context5': var5})
