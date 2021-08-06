from django.urls import path
from .views import *


urlpatterns = [
    path('contact/', contact_view, name='contact'),
]