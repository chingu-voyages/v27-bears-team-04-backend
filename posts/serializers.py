from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Class to transforms Post models into json data"""

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post
