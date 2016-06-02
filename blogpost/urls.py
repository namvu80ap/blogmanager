from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogpost.views import Index, ArticleList, ArticleDetail, EditArticleView, ListArticleView


article_urls = [
    # url(r'^/(?P<pk>\d+)/photos$', ArticlePhotoList.as_view(), name='postphoto-list'),
    url(r'^(?P<pk>\d+)$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^$', ArticleList.as_view(), name='article-list'),
]

urlpatterns = [
	url(r'^$', Index.as_view()),
	url(r'^edit_article.html$',  EditArticleView.as_view()),
	url(r'^list_article.html$', ListArticleView.as_view()),
    url(r'^articles', include(article_urls)),
]
