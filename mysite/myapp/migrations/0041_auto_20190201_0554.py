# Generated by Django 2.1.5 on 2019-02-01 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_auto_20190201_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='picture',
            new_name='img_up',
        ),
    ]
