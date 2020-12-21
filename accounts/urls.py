from django.urls import path

from .views import SignUpView, vm_charts
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', vm_charts, name='vm_charts'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]