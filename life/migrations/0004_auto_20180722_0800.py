# Generated by Django 2.0.7 on 2018-07-22 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0003_auto_20180722_0523'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='item',
            name='date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='purchasedBy',
        ),
        migrations.AlterField(
            model_name='item',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life.User'),
        ),
    ]
