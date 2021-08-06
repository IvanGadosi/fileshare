from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

from fileshare.models import SharedFile


class PricingView(TemplateView):
    template_name="pricing.html"
    

class PaypalView(FormView):
    template_name='paypal.html'
    form_class=PayPalPaymentsForm

    def get_initial(self):

        return {
            "business": 'send-money-to@example.com',
            "amount": 5,
            "currency_code": "EUR",
            "item_name": self.kwargs['pk'],
            "invoice": self.kwargs['pk'],
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'

class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'

