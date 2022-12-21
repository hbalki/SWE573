from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import safe, slugify
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from taggit.managers import TaggableManager
from django.utils.timezone import timezone

class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=50, blank=False, null=True, verbose_name='İsim Giriniz', help_text= 'İsim Bilgisi Burada Girilir.')
    surname = models.CharField(max_length=50, blank=False, null=True, verbose_name='Soyisim Giriniz', help_text= 'Soyisim Bilgisi Burada Girilir.')
    email = models.EmailField(max_length=50, blank=False, null=True, verbose_name='Email Giriniz')
    email2 = models.EmailField(max_length=50, blank=False, null=True, verbose_name="Email'i tekrar giriniz")
    content = models.TextField(max_length=50, blank=False, null=True, verbose_name="İçerik giriniz", help_text= "İçerik Bilgisi Burada Girilir.")

    class Meta:
        verbose_name = 'Registration'

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})





class Blog(models.Model):
    CATEGORY_CHOICES = ((None, 'Please select an option'), ('art', 'ART'), ('science', 'SCIENCE'), ('sports', 'SPORTS'), ('photography', 'PHOTOGRAPHY'), ('technology', 'TECHNOLOGY'), ('travel', 'TRAVEL'), ('other', 'OTHER'))
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Title', help_text='Title of the blog')
    category_choices = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null= True, blank= False, verbose_name='Select a Category', help_text='Select a category for your blog')
    link = models.URLField(max_length=1000, blank=True, null=True, verbose_name='link', help_text='Link of the blog')
    content = models.CharField(max_length=1000, blank=False, null=True, verbose_name='Description', help_text='Description of the blog')
    image = models.ImageField(default='default/default_img.jpg', blank=True, null=True, verbose_name='Load an image', help_text='Load an image for your blog')
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    tags = TaggableManager()
    slug = models.SlugField(max_length=100, unique=True)
    # new_field_2 = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, null=True, blank=True, related_name='new_field')

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-created_date']

    def __str__(self):
        return "%s" % self.title

    # @classmethod
    #
    # def get_choices(cls, categories):
    #     return cls.objects.filter(category_choices=categories)



    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})     

    def get_image(self):

        if self.image:
            return self.image.url
        #
        # elif self.get_image(html):
        #     return self.get_image(html)

        else:
            return '/media/default/default_img.jpg'

    def get_category_choices_html(self):
        if self.category_choices == 'all':
            return safe('<span class="badge badge-pill badge-light">ART</span>')
        if self.category_choices == 'art':
            return safe('<span class="badge badge-pill badge-primary">ART</span>')
        elif self.category_choices == 'science':
            return safe('<span class="badge badge-pill badge-success">SCIENCE</span>')
        elif self.category_choices == 'sports':
            return safe('<span class="badge badge-pill badge-danger">SPORTS</span>')
        elif self.category_choices == 'photography':
            return safe('<span class="badge badge-pill badge-warning">PHOTOGRAPHY</span>')
        elif self.category_choices == 'technology':
            return safe('<span class="badge badge-pill badge-info">TECHNOLOGY</span>')
        elif self.category_choices == 'travel':
            return safe('<span class="badge badge-pill badge-secondary">TRAVEL</span>')
        elif self.category_choices == 'other':
            return safe('<span class="badge badge-pill badge-dark">OTHER</span>')
        else:
            return safe('<span class="badge badge-pill badge-light">Please select an option</span>')



    def get_blog_comment(self):
        return self.comment.all()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=True, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField(max_length=1000, help_text='Yorumunuzu buraya giriniz')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['created_on']

    def __str__(self):
        # return 'Comment {} by {}'.format(self.content, self.email)
        return '%s %s' % (self.email, self.blog)

    def get_screen_name(self):
        if self.name and self.surname:
            return '{} {}'.format(self.name, self.surname)
        return self.email

