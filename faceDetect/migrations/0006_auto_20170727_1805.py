# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceDetect', '0005_auto_20170708_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturedata',
            name='file2',
            field=models.ImageField(default='False2.jpg', upload_to='kinImgs'),
        ),
        migrations.AlterField(
            model_name='picturedata',
            name='file',
            field=models.ImageField(default='False.jpg', upload_to='kinImgs'),
        ),
    ]
