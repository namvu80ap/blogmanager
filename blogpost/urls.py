from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogpost.views import Index

urlpatterns = [
	url(r'^$', Index.as_view()),
]