# Generated by Django 2.1.5 on 2019-02-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_auto_20190204_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodels',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]