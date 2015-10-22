# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_newuser_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=5)),
                ('section', models.CharField(max_length=1, choices=[(b'A', b'Section A'), (b'B', b'Section B')])),
            ],
        ),
    ]
