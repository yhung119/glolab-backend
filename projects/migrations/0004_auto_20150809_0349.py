# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(default=b'img/%Y/%m/%d.jpg', upload_to=b'project_image', blank=True),
        ),
    ]
