from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import safe
from taggit.managers import TaggableManager
from unidecode import unidecode
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField




class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=50, blank=False, null=True, verbose_name='İsim Giriniz',
                            help_text='İsim Bilgisi Burada Girilir.')
    surname = models.CharField(max_length=50, blank=False, null=True, verbose_name='Soyisim Giriniz',
                               help_text='Soyisim Bilgisi Burada Girilir.')
    email = models.EmailField(max_length=50, blank=False, null=True, verbose_name='Email Giriniz')
    email2 = models.EmailField(max_length=50, blank=False, null=True, verbose_name="Email'i tekrar giriniz")
    content = models.TextField(max_length=50, blank=False, null=True, verbose_name="İçerik giriniz",
                               help_text="İçerik Bilgisi Burada Girilir.")

    class Meta:
        verbose_name = 'Registration'

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.title = None
        self.slug = None

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Blog(models.Model):
    CATEGORY_CHOICES = ((None, 'Please select an option'), ('art', 'ART'), ('science', 'SCIENCE'), ('sports', 'SPORTS'),
                        ('photography', 'PHOTOGRAPHY'), ('technology', 'TECHNOLOGY'), ('travel', 'TRAVEL'),
                        ('other', 'OTHER'))
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Title',
                             help_text='Title of the blog')
    category_choices = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=False,
                                        verbose_name='Select a Category', help_text='Select a category for your blog')
    link = models.URLField(max_length=1000, blank=True, null=True, verbose_name='link', help_text='Link of the blog')
    content = RichTextField(max_length=5000, blank=False, null=True, verbose_name='Description')
    image = models.ImageField(default='default/default_img.jpg', blank=True, null=True, verbose_name='Load an image',
                              help_text='Load an image for your blog')
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    # tags = TaggableManager()
    slug = models.SlugField(max_length=100, null=True, unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-created_date']

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        num = 1
        slug = slugify(unidecode(self.title))
        new_slug = slug

        while Blog.objects.filter(slug=new_slug).exists():
            num += 1
            new_slug = "{}-{}".format(slug, num)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()

        else:
            blog = Blog.objects.get(slug=self.slug)
            if blog.title != self.title:
                self.slug = self.get_unique_slug()
        super(Blog, self).save(*args, **kwargs)

    # def link_query(self):
    #     if self.link is not None:
    #         return reverse('preview', kwargs={'slug': self.slug})

    def get_image(self):

        if self.image:
            return self.image.url

        # elif get_image():
        #     return get_image()

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
