import os

from django.db import models


class FinishedPhoto(models.Model):
    photo = models.ImageField(upload_to='finished_photos')
    uuid = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()

    @property
    def filename(self):
        return os.path.basename(self.photo.file.name)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('calvin.apps.temperature.views.photo', args=[str(self.uuid)])
