# Generated by Django 3.1.7 on 2021-03-24 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210324_1446'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='NewsCategory',
        ),
    ]