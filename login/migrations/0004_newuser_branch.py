# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='branch',
            field=models.CharField(default=b'', max_length=5),
        ),
    ]
