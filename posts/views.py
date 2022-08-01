from django.contrib.auth import get_user_model
from rest_framework import viewsets  # new
from rest_framework.permissions import IsAdminUser  # new

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

# viewset
class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    permission_classes = [IsAdminUser]  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# normal views
# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAdminUser,)  # new
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
