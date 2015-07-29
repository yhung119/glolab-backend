# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0003_auto_20150728_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(default=b'', max_length=450, blank=True),
        ),
    ]
