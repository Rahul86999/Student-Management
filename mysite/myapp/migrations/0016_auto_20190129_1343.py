# Generated by Django 2.1.5 on 2019-01-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='model_pic',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]