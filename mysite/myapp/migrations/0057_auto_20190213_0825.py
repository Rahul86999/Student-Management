# Generated by Django 2.1.5 on 2019-02-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0056_auto_20190213_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employemodel',
            name='item_select',
            field=models.CharField(choices=[('"Not relevant"', 'Not relevant'), ('Review', 'Review'), ('Maybe relevant', 'Maybe relevant'), ('Relevant', 'Relevant'), ('Leading candidate', 'Leading candidate')], default='dsjf', max_length=50),
        ),
    ]