# Generated by Django 2.1.5 on 2019-01-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20190129_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='img_up',
            field=models.ImageField(default='album_logos/no-image.jpg', upload_to='images'),
        ),
    ]
