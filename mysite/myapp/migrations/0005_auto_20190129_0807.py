# Generated by Django 2.1.5 on 2019-01-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190129_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
