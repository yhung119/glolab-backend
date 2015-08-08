# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='companyprofile',
            field=models.ForeignKey(default=1, to='userpro.CompanyProfile'),
            preserve_default=True,
        ),
    ]
