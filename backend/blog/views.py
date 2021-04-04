from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Post
from .serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer