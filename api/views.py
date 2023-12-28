from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Todos, Comment, Post
from .serializers import UserSerializer, TodosSerializer, CommentSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Usuários
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodosViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Todos
    """
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer