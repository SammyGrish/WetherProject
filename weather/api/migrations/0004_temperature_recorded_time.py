# Generated by Django 2.1.5 on 2019-01-31 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190123_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='recorded_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
