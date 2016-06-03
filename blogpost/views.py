from django.shortcuts import render, render_to_response
from django.views.generic import View
from rest_framework import generics, authentication, permissions, viewsets, filters
from blogpost.models import Article
from blogpost.dataserializer import ArticleSerializer
from blogpost.permissions import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
import logging
import logging.handlers
from django.conf import settings

logger = logging.getLogger('blogpost')

class Index(View):
	def get(self, request):
		params = {}
		params["name"] = "Django"
		return render(request, 'blogpost/main.html', params)

class EditArticleView(View):
	def get(self, request):
		return render(request, 'blogpost/edit_article.html')

class ListArticleView(View):
	def get(self, request):
		return render(request, 'blogpost/list_article.html')


# API Class and methoss
class DefaultsMixin(object):
	# logger.debug( 'DefaultsMixin --> '  +  object )
	# request.user.is_authenticated()
	# authentication_classes = (
	# 	authentication.SessionAuthentication,
	# )
	# permission_classes = (
	# 	permissions.IsAuthenticated,
	# )

	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

	filter_backends = (
		filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter,
    )

class ArticlePost(DefaultsMixin, viewsets.ModelViewSet):
	"""API endpoint for listing and creating Articles."""
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

    # filter_class = ArticleFilter
	# search_fields = ('name', )
	# ordering_fields = ('end', 'name', )

# class ArticlePost(object):
#     model = Article
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleList(ArticlePost, generics.ListCreateAPIView):
#     pass


# class ArticleDetail(ArticlePost, generics.RetrieveUpdateDestroyAPIView):
#     pass
# class Index(View):
# 	def get(self, request):
# 		return HttpResponse('I am called from a get Request')
# 	def post(self, request):
# 		return HttpResponse('I am called from a post Request')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/blogpost/')