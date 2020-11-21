# Generated by Django 3.1.3 on 2020-11-21 18:58

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('slug', models.SlugField(max_length=500)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=False, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modification_date', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_users', related_query_name='article_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]