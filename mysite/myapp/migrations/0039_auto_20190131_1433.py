# Generated by Django 2.1.5 on 2019-01-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_auto_20190131_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(height_field='width', max_length=255, null=True, upload_to='gallery', width_field='height'),
        ),
    ]