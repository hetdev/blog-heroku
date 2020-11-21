from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(null=False,
                             blank=False,
                             max_length=400)
    slug = models.SlugField(null=False,
                            blank=False,
                            max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                               blank=False,
                               related_name='article_users',
                               related_query_name='article_user'
                               )
    content = models.TextField(null=False,
                               blank=False)

    publication_date = models.DateTimeField(null=True, blank=False)
    active = models.BooleanField(null=True, blank=False, default=False)

    creation_date = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    last_modification_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{str(self.title)}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class ContactRequest(models.Model):
    name = models.CharField(null=False,
                            blank=False,
                            max_length=200)
    email = models.EmailField(null=False,
                              blank=False,
                              max_length=200)
    content = models.TextField(null=False,
                               blank=False)

    contact_date = models.DateTimeField(null=True, blank=True)

    creation_date = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    last_modification_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{str(self.name)} - {str(self.email)}'