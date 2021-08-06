from django.db import models
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch.dispatcher import receiver

from fileshare.models import SharedFile


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != 'send-money-to@example.com':
            return
        try:
            my_pk = ipn_obj.invoice
            mytransaction = SharedFile.objects.get(pk=my_pk)
            assert ipn_obj.mc_gross == 5 and ipn_obj.mc_currency == 'EUR'
        except Exception:
            logger.exception('Paypal ipn_obj data not valid!')
        else:
            mytransaction.paid = True
            mytransaction.save()
    else:
        logger.debug('Paypal payment status not completed: {}'.format(ipn_obj.payment_status))