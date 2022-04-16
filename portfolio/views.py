from django.conf import settings
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'