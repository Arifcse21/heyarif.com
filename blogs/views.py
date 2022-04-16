from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_at')[:7]
    print(Post.objects.all().count())
    
    template_name = 'portfolio/index.html'



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'portfolio/detail.html'