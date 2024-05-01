# Generated by Django 5.0.4 on 2024-04-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='location',
            field=models.CharField(default='TBD', max_length=255),
        ),
        migrations.AddField(
            model_name='club',
            name='meeting_times',
            field=models.CharField(default='TBD', max_length=255),
        ),
        migrations.AddField(
            model_name='club',
            name='sponsor_email',
            field=models.CharField(default='TBD', max_length=255),
        ),
        migrations.AddField(
            model_name='club',
            name='sponsor_name',
            field=models.CharField(default='TBD', max_length=255),
        ),
    ]
