# Generated by Django 3.0 on 2020-03-16 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_todomodel_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todomodel',
            options={'ordering': ['-date_created']},
        ),
    ]
