from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    re_path('(?P<path>.*)$',
            TemplateView.as_view(template_name='ui/react-flux.index.html')),
]
