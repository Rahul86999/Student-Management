# Generated by Django 2.1.5 on 2019-01-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20190131_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
