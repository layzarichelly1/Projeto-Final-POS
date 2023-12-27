from rest_framework import serializers
from .models import User, Todo, Comment, Post

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'