# Generated by Django 2.1.5 on 2019-01-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20190131_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(height_field='width', max_length=255, upload_to='gallery', width_field='height'),
        ),
    ]
