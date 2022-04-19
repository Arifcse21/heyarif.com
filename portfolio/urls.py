from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import PostList, PostDetail

urlpatterns=[
    path('',PostList.as_view(), name='home'),
    path('blogs/<slug:slug>',PostDetail.as_view(), name='post_detail'),
]
