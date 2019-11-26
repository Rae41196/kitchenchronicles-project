# Generated by Django 2.2.7 on 2019-11-22 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_post_category', models.CharField(blank=True, max_length=50)),
                ('blog_title', models.CharField(help_text='Enter Blog Title', max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('blog_content', models.TextField(help_text='Type Your Post Here')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish'), ('w', 'Withdrawn')], max_length=1)),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['blog_author', '-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name', max_length=80)),
                ('email', models.EmailField(blank=True, help_text='Your Email', max_length=254)),
                ('body', models.TextField(help_text='Your comment')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='foodieblog.Post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
