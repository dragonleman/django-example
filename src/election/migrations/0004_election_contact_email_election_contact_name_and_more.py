# Generated by Django 4.2.2 on 2023-06-19 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_alter_election_maxchoices'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='contact_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='election',
            name='contact_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='election',
            name='contact_phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='election',
            name='enddate',
            field=models.CharField(default=datetime.date(2023, 6, 19), max_length=50),
        ),
        migrations.AddField(
            model_name='election',
            name='startdate',
            field=models.CharField(default=datetime.date(2023, 6, 19), max_length=50),
        ),
        migrations.AlterField(
            model_name='election',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
