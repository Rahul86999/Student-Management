# Generated by Django 2.1.5 on 2019-01-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190129_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=2),
        ),
    ]