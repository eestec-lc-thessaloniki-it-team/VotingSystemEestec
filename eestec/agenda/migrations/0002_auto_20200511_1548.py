# Generated by Django 3.0.6 on 2020-05-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]