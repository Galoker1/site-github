# Generated by Django 3.1.3 on 2021-01-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='hrefbook',
            field=models.TextField(blank=True),
        ),
    ]
