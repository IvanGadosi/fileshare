from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('successful-upload/<str:pk>/', success_view, name='success'),
    path('files/<str:pk>/', search_result_view, name='search-result'),
]