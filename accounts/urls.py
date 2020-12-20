from django.urls import path

from .views import SignUpView, RiskRatingChart
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', RiskRatingChart, name='risk_chart'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]