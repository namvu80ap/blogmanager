from rest_framework import serializers

from blogpost.models import Category, Article

class ArticleSerializer(serializers.ModelSerializer):
    # photos = serializers.HyperlinkedIdentityField('photos', view_name='postphoto-list')
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(ArticleSerializer, self).get_validation_exclusions()
        return exclusions

    class Meta:
        model = Article