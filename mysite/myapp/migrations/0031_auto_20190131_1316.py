# Generated by Django 2.1.5 on 2019-01-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20190131_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
