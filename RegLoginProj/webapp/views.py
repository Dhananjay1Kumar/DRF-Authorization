from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
