# Generated by Django 4.1.3 on 2022-12-19 22:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_category_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, verbose_name='İçerik Giriniz'),
        ),
    ]
