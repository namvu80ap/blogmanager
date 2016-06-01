from django.shortcuts import render
from django.views.generic import View

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
		return render(request, 'blogpost/base.html', params)

# class Index(View):
# 	def get(self, request):
# 		return HttpResponse('I am called from a get Request')
# 	def post(self, request):
# 		return HttpResponse('I am called from a post Request')