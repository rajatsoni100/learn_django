# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 21, 6, 46, 53, 809451, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
