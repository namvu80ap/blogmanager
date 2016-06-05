from django.shortcuts import render, render_to_response
from django.views.generic import View
from rest_framework import generics, authentication, permissions, viewsets, filters
from blogpost.models import Article, Photo, Tag
from blogpost.dataserializer import ArticleSerializer, PhotoSerializer, TagSerializer
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
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
from rest_framework.parsers import FileUploadParser
from blogmanager.settings import BASE_DIR
logger = logging.getLogger('blogpost')

class Index(View):
	def get(self, request):
		params = {}
		params["name"] = "Django"
		return render(request, 'blogpost/main.html', params)

class EditArticleView(View):
	def get(self, request):
		return render(request, 'blogpost/edit_article.html')

class AddArticleView(View):
    def get(self, request):
        return render(request, 'blogpost/add_article.html')

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
        serializer = ArticleSerializer(article, context={'request': request}, many=True)
        return Response(serializer.data)

    # def get_object(self, pk):
    #     try:
    #         return Article.objects.get(pk=pk)
    #     except Article.DoesNotExist:
    #         raise Http404

    @method_decorator(csrf_protect)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(DefaultsMixin,APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    @method_decorator(csrf_protect)
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)

    @method_decorator(csrf_protect)
    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoPost(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class TagPost(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

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

def photouUpload(request):
    up_file = request.FILES['file']
    articleId = request.POST['articleId']
    # logger.debug(articleId);
    imageUrl = BASE_DIR + '/media/' + articleId + '_' + up_file.name
    destination = open( imageUrl, 'wb+')
    for chunk in up_file.chunks():
        destination.write(chunk)
        destination.close()
    #Create Photo data
    photo = Photo( article_id = articleId , imageUrl = imageUrl ,  photo_name = up_file.name )
    photo.save() 
    return HttpResponse("File upload success")

def deleteArticleTag(request):
    articleId = request.POST['articleId']
    
    article = Article.objects.get(id = articleId)
    article.tags.all().delete()

    return HttpResponse("success")
# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser, )

#     def post(self, request, format='jpg'):
#         up_file = request.FILES['file']
#         destination = open('/home/aimi/Projects/blogmanager/' + up_file.name, 'wb+')
#         for chunk in up_file.chunks():
#             destination.write(chunk)
#             destination.close()

#         return Response(up_file.name, status.HTTP_201_CREATED)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/blogpost/')