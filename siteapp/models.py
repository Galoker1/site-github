from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    title=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(max_length=150,unique=True)
    text=models.TextField(blank=True,db_index=True)
    image=models.TextField()
    rate=models.TextField()
    hrefbook=models.TextField(blank=True)

    def rate_plus():
        rate+=1
    def get_absolute_url(self):
        return reverse('book_detail_url',kwargs={'slug':self.slug})


    def __str__(self):
        return self.title
