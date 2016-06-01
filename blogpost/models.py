from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=2500)

class Article(models.Model):
	category = models.ForeignKey('Category' , on_delete=models.CASCADE, related_name='articles')
	title = models.CharField(max_length=250)
	content = models.TextField(max_length=2500)

class Tag(models.Model):
	articles = models.ManyToManyField("Article")
	name = models.CharField(max_length=200, default='')

class Photo(models.Model):
    articles = models.ForeignKey('Article', related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")