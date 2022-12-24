# Generated by Django 4.1.3 on 2022-12-20 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(help_text='Yorumunuzu buraya giriniz', max_length=1000),
        ),
    ]
