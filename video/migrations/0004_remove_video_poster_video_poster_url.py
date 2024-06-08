# Generated by Django 4.1.1 on 2022-09-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='poster',
        ),
        migrations.AddField(
            model_name='video',
            name='poster_url',
            field=models.TextField(default='defalut.jpg', max_length=50),
            preserve_default=False,
        ),
    ]
