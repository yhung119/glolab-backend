# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0003_auto_20150810_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='project_a',
            field=models.SlugField(default=b''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project_b',
            field=models.SlugField(default=b''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'project_image', blank=True),
        ),
    ]
