# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 03:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sleep', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SleepRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DR', to='device.Device')),
                ('report', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.CASCADE, related_name='RR', to='sleep.Report')),
                ('sleep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SR', to='sleep.Sleep')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UR', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
