# Generated by Django 2.1.5 on 2021-11-26 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20211126_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardtable',
            name='board_dt',
            field=models.DateField(default=datetime.datetime(2021, 11, 26, 17, 26, 6, 121055)),
        ),
        migrations.AlterField(
            model_name='boardtable',
            name='board_up_dt',
            field=models.DateField(default=datetime.datetime(2021, 11, 26, 17, 26, 6, 121075)),
        ),
    ]