# Generated by Django 3.0.6 on 2020-05-30 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0007_auto_20200527_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destdescription',
            name='place_description',
        ),
    ]
