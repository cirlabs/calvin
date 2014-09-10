import logging

from django.http import JsonResponse
from django.core.management import call_command

logger = logging.getLogger('cir.custom')


def yo_view(request):
    logger.info("Yo.")
    call_command('get_current_temp', interactive=True)
    return JsonResponse({'foo': 'bar'})
