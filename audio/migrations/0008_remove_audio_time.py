# Generated by Django 4.1.1 on 2022-09-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_alter_audio_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='time',
        ),
    ]
