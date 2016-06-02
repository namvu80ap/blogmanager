from django.shortcuts import render
from django.views.generic import View
from rest_framework import generics, permissions
from blogpost.models import Article
from blogpost.dataserializer import ArticleSerializer
from blogpost.permissions import *

# def index(request):
# 	params = {}
# 	params["name"] = "Dai Ca Nam"
# 	template = loader.get_template('blogpost/index.html')
#     # return HttpResponse("Hello, world. You're at the polls index.")
# 	return HttpResponse(template.render(params, request))
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

	# def edit_article(request):
 # 		return render(request, 'blopost/edit_article.html')
 # 	def list_article(request):
 # 		return render(request, 'blopost/list_article.html')


# class ArticleList(generics.ListCreateAPIView):
#     model = Article
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]


class ArticlePost(object):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
        # PostAuthorCanEditPermission
        permissions.AllowAny
    ]

    # def perform_create(self, serializer):
    #     """Force author to the current user on save"""
    #     serializer.save(author=self.request.user)


class ArticleList(ArticlePost, generics.ListCreateAPIView):
    pass


class ArticleDetail(ArticlePost, generics.RetrieveUpdateDestroyAPIView):
    pass
# class Index(View):
# 	def get(self, request):
# 		return HttpResponse('I am called from a get Request')
# 	def post(self, request):
# 		return HttpResponse('I am called from a post Request')