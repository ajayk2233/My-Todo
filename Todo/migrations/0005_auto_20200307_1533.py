# Generated by Django 3.0 on 2020-03-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0004_auto_20200307_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
