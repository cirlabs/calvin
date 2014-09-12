# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishedphoto',
            name='uuid',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finishedphoto',
            name='photo',
            field=models.ImageField(upload_to=b'finished_photos'),
        ),
    ]
