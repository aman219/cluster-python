# Generated by Django 4.1.1 on 2022-09-15 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 15, 28, 47, 105731, tzinfo=datetime.timezone.utc), editable=False),
            preserve_default=False,
        ),
    ]
