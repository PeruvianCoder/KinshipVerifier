# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 23:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceDetect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picturedata',
            old_name='image1',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='picturedata',
            old_name='image2',
            new_name='img2',
        ),
    ]
