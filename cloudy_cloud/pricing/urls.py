from django.urls import path
from .views import *


urlpatterns = [
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('paypal/<str:pk>/', PaypalView.as_view(), name='paypal-buy'),
    path('paypal-return/', PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', PaypalCancelView.as_view(), name='paypal-cancel'),
]