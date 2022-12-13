from django.db import models
from django.shortcuts import reverse

class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık Giriniz', help_text='Başlık '

                                                                                                            'Bilgisi Burada Girilir.')
    link = models.URLField(max_length=1000, blank=False, null=True, verbose_name='Bağlantı adresini giriniz')
    content = models.TextField(max_length=1000, blank=False, null=True, verbose_name='İçerik Giriniz')
    created_date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


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

