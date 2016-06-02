from rest_framework import serializers

from blogpost.models import Category, Article

class ArticleSerializer(serializers.ModelSerializer):
    def get_validation_exclusions(self):
        exclusions = super(ArticleSerializer, self).get_validation_exclusions()
        return exclusions

    class Meta:
        model = Article