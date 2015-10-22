# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20151022_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='branch',
            field=models.ForeignKey(to='login.Branch'),
        ),
    ]
