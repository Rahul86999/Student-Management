# Generated by Django 2.1.5 on 2019-02-07 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_employemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employemodel',
            old_name='emp_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='employemodel',
            old_name='emp_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employemodel',
            old_name='emp_qualification',
            new_name='qualification',
        ),
    ]
