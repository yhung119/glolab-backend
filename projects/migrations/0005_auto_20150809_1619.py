# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150809_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(upload_to=b'project_image', blank=True),
        ),
    ]
