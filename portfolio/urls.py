from portfolio.views import IndexView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',IndexView.as_view(), name='home'),
]
