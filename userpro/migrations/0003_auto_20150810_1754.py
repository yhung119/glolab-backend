# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0002_companyprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
    ]
