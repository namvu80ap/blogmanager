from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField, SlugRelatedField
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from blogpost.models import Category, Article, Photo, Tag

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
	photos = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='photo_name'
	)

	tags = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='name'
	)

	class Meta:
		model = Article
		fields = ('id', 'category', 'title', 'content', 'photos' , 'tags' )

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = ('id', 'article', 'photo_name', 'imageUrl', )

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'article', 'name' )