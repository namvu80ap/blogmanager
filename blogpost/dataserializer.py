from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from blogpost.models import Category, Article

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
	# links = serializers.SerializerMethodField()
    # def get_validation_exclusions(self):
    #     exclusions = super(ArticleSerializer, self).get_validation_exclusions()
    #     return exclusions
	class Meta:
		model = Article
		fields = ('id', 'category', 'title', 'content', )
	# def get_links(self, obj):
	# 	# request = self.context['request']
	# 	request = self.context.request
	# 	return {
	# 		'self': reverse('article-detail',kwargs={'pk': obj.pk}, request=request),
 #        }