from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify, safe

class Blog(models.Model):
    objects = None
    CATEGORY_CHOICES = (('art', 'ART'), ('science', 'SCIENCE'), ('sports', 'SPORTS'), ('photography', 'PHOTOGRAPHY'), ('technology', 'TECHNOLOGY'), ('travel', 'TRAVEL'), ('other', 'OTHER'))
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık Giriniz', help_text='Başlık '

                                                                                                            'Bilgisi Burada Girilir.')
    category_choices = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name='Kategori Seçiniz', help_text='Kategori ')
    link = models.URLField(max_length=1000, blank=True, null=True, verbose_name='Bağlantı adresini giriniz')
    content = models.TextField(max_length=1000, blank=False, null=True, verbose_name='İçerik Giriniz')
    image = models.ImageField(default='default/default_img.jpg', blank=True, null=True, verbose_name='Resim Yükleyiniz')
    created_date = models.DateField(auto_now_add=True, auto_now=False)


    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})     

    def get_image(self):
        # if generate_preview(request=True) and not self.get_image(html=True):
        #     return '/media/default/default_img.jpg'

        if self.image:
            return self.image.url

        else:
            return '/media/default/default_img.jpg'

    def get_color_html(self):
        if self.category_choices == 'art':
            return '<small style="color: white; background-color: red">ART</small>'
        elif self.category_choices == 'science':
            return '<small style="color: white; background-color: blue">SCIENCE</small>'
        elif self.category_choices == 'sports':
            return '<small style="color: white; background-color: green">SPORTS</small>'
        elif self.category_choices == 'photography':
            return '<small style="color: black; background-color: yellow">PHOTOGRAPHY</small>'
        elif self.category_choices == 'technology':
            return '<small style="color: white; background-color: purple">TECHNOLOGY</small>'
        elif self.category_choices == 'travel':
            return '<small style="color: black; background-color: orange">TRAVEL</small>'
        else:
            return '<small style="color: white; background-color: darkblue">OTHER</small>'



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

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})

