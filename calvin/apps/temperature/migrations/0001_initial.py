# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=None)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('temperature', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
