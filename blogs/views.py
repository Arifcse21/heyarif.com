from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_at')[:7]
    
    template_name = 'portfolio/index.html'

class PostListAll(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_at')
    paginate_by = 2
    template_name = 'blogs/posts_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'