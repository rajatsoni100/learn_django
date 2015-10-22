# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151022_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='branch',
            field=models.CharField(default=b'', max_length=5, choices=[(b'CSE', b'Computer Science'), (b'IT', b'Info Tech')]),
        ),
    ]
