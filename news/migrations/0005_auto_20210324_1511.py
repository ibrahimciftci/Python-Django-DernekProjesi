# Generated by Django 3.1.7 on 2021-03-24 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210324_1455'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='News',
        ),
    ]
