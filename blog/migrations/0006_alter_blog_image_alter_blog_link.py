# Generated by Django 4.1.3 on 2022-12-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_contact_image_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default/default_img.jpg', null=True, upload_to='', verbose_name='Resim Yükleyiniz'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Bağlantı adresini giriniz'),
        ),
    ]