# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='picture',
            field=models.ImageField(default=datetime.datetime(2015, 8, 10, 17, 53, 53, 742849, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
