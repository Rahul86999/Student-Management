# Generated by Django 2.1.5 on 2019-02-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0057_auto_20190213_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employemodel',
            name='item_select',
            field=models.CharField(choices=[('"--Select--"', '--Select--'), ('Java', 'Java'), ('Python', 'Python'), ('Web Desining', 'Web Desining'), ('PHP', 'PHP')], default='dsjf', max_length=50),
        ),
    ]
