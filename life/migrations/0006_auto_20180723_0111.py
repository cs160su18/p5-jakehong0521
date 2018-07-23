# Generated by Django 2.0.7 on 2018-07-23 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_auto_20180722_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='addedBy',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(default=datetime.date(2018, 7, 23)),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
