from django.urls import path

from .views import SignUpView, RiskRatingChart

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', RiskRatingChart, name='risk_chart'),
]