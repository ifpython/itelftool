# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appconf', '0003_auto_20180823_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokenRrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='故障名称')),
                ('description', models.CharField(max_length=255, verbose_name='故障描述')),
                ('process_description', models.TextField(verbose_name='处理过程')),
                ('precaution', models.CharField(blank=True, max_length=255, null=True, verbose_name='预防措施')),
                ('broken_type', models.CharField(choices=[('Network', 'Network'), ('CDN', 'CDN'), ('Other', 'Other')], max_length=30, verbose_name='故障类型')),
                ('severity_type', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=30, verbose_name='故障严重性')),
                ('broken_status_type', models.CharField(choices=[('Solved', 'Solved'), ('Processing', 'Processing'), ('Shelving', 'Shelving')], max_length=30, verbose_name='故障状态类型')),
                ('broken_department', models.CharField(choices=[('Maintenance_department', 'Maintenance_department'), ('Technical_department', 'Technical_department'), ('other', 'other')], max_length=30, verbose_name='故障归属部门')),
                ('occur_time', models.DateTimeField(verbose_name='故障发生时间')),
                ('end_time', models.DateTimeField(verbose_name='故障结束时间')),
                ('business_impact_time', models.CharField(max_length=50, verbose_name='业务影响时间')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='开发人员')),
                ('phone', models.CharField(max_length=50, verbose_name='开发人员手机')),
                ('qq', models.CharField(blank=True, max_length=100, null=True, verbose_name='开发人员QQ')),
                ('weChat', models.CharField(blank=True, max_length=100, null=True, verbose_name='开发人员微信')),
            ],
        ),
        migrations.AddField(
            model_name='brokenrrecord',
            name='developer',
            field=models.ManyToManyField(blank=True, null=True, to='broken_record.Developer', verbose_name='开发处理人'),
        ),
        migrations.AddField(
            model_name='brokenrrecord',
            name='maintenance',
            field=models.ManyToManyField(blank=True, null=True, to='appconf.AppOwner', verbose_name='运维处理人'),
        ),
        migrations.AddField(
            model_name='brokenrrecord',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appconf.Project', verbose_name='所属项目'),
        ),
    ]