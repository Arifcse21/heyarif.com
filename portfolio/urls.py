from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name='index'),
    # path('thanks/',views.thanks, name='thanks')
]
