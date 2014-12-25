# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Description',
            field=models.TextField(default=datetime.datetime(2014, 12, 25, 5, 34, 40, 403815, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
