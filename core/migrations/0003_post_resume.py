# Generated by Django 3.1.6 on 2021-03-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210313_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.TextField(default=''),
        ),
    ]
