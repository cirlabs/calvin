import logging
from StringIO import StringIO

from django.http import JsonResponse, HttpResponse
from django.core.management import call_command
from .models import FinishedPhoto

logger = logging.getLogger('cir.custom')


def yo_view(request):
    logger.info("Yo.")

    content = StringIO()
    call_command('get_current_temp', interactive=True, stdout=content)
    content.seek(0)
    return JsonResponse({'img_id': content.read().replace('\n', '')})


def photo(request, uuid):
    try:
        obj = FinishedPhoto.objects.get(uuid=uuid)
        image_data = open(obj.photo.file.name, "rb").read()
        return HttpResponse(image_data, content_type="image/jpeg")
    except:
        raise
