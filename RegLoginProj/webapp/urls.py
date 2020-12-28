from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList,UserDetail, PostList, PostDetail

app_name= 'webapp'

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)