# Generated by Django 2.1.5 on 2019-01-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20190131_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
