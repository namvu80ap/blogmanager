from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogpost.views import *
from django.contrib.auth.decorators import login_required

from rest_framework.routers import DefaultRouter

# article_urls = [
    # url(r'^/(?P<pk>\d+)/photos$', ArticlePhotoList.as_view(), name='postphoto-list'),
    # url(r'^(?P<pk>\d+)$', login_required(ArticleDetail.as_view()), name='article-detail'),
    # url(r'^$', login_required(ArticlePost.as_view()), name='article-list'),
# ]

# API rounter
router = DefaultRouter()
router.register(r'photo', PhotoPost)
router.register(r'tag', TagPost)
# router.register(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

urlpatterns = [
	url(r'^accounts/login/$', 'django.contrib.auth.views.login' , name='login'),
    url(r'^logout/$', 'blogpost.views.logout_page' , name='logout' ),
	url(r'^$', login_required(Index.as_view()) ),
	url(r'^edit_article.html$',  login_required(EditArticleView.as_view())),
	url(r'^add_article.html$',  login_required(AddArticleView.as_view())),
	url(r'^list_article.html$', login_required(ListArticleView.as_view())),
    url(r'^articles/$', ArticlePost.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    # url(r'^articles', include(article_urls)),
    url(r'^photoUpload/$', photouUpload , name='photouUpload'),
    url(r'^deleteArticleTag/$', deleteArticleTag , name='deleteArticleTag'),
    # Simple router
    url(r'^', include(router.urls)),
]
