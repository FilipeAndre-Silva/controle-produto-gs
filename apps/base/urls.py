from django.urls import path
from apps.base.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
]