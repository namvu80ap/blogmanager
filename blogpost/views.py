from django.shortcuts import render, render_to_response
from django.views.generic import View
from rest_framework import generics, authentication, permissions, viewsets, filters
from blogpost.models import Article
from blogpost.dataserializer import ArticleSerializer
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
import logging
import logging.handlers
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator


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
	authentication_classes = (
		authentication.SessionAuthentication,
	)
	permission_classes = (
		permissions.IsAuthenticated,
	)
	paginate_by = 2
	paginate_by_param = 'page_size'
	max_paginate_by = 2

	filter_backends = (
		filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter,
    )


class ArticlePost(DefaultsMixin, APIView):
    @method_decorator(csrf_protect)
    def get(self, request, format=None):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

class ArticleDetail(DefaultsMixin,APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @method_decorator(csrf_protect)
    def put(self, request, pk, format=None):
        logger.debug(request.user)
        logger.debug(request.user.is_authenticated())
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class ArticlePost(viewsets.ModelViewSet):
# 	"""API endpoint for listing and creating Articles."""
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerializer

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