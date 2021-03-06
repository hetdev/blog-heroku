# Generated by Django 3.1.3 on 2020-11-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_contactrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='contact_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
