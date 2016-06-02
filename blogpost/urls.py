from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogpost.views import Index, ArticleList, ArticleDetail, EditArticleView, ListArticleView
from django.contrib.auth.decorators import login_required

article_urls = [
    # url(r'^/(?P<pk>\d+)/photos$', ArticlePhotoList.as_view(), name='postphoto-list'),
    url(r'^(?P<pk>\d+)$', login_required(ArticleDetail.as_view()), name='article-detail'),
    url(r'^$', login_required(ArticleList.as_view()), name='article-list'),
]

urlpatterns = [
	url(r'^accounts/login/$', 'django.contrib.auth.views.login' , name='login'),
    url(r'^logout/$', 'blogpost.views.logout_page' , name='logout' ),
	url(r'^$', login_required(Index.as_view()) ),
	url(r'^edit_article.html$',  login_required(EditArticleView.as_view())),
	url(r'^list_article.html$', login_required(ListArticleView.as_view())),
    url(r'^articles', include(article_urls)),
]
