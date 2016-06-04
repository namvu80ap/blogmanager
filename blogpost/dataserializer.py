from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField, SlugRelatedField
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from blogpost.models import Category, Article, Photo

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
	photos = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='photo_name'
	)

	class Meta:
		model = Article
		fields = ('id', 'category', 'title', 'content', 'photos' )

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = ('id', 'article', 'photo_name', 'imageUrl', )