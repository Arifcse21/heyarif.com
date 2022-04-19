from django.urls import path
from blogs.views import PostListAll, PostDetail
urlpatterns = [
   path('blogs/', PostListAll.as_view(), name='blogs'),
   path('blogs/<slug:slug>', PostDetail.as_view(), name='post_detail'),
]
