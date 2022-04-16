from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import PostList

urlpatterns=[
    path('',PostList.as_view(template_name='portfolio/index.html')),
]
