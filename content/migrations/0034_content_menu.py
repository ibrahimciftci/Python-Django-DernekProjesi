# Generated by Django 3.1.7 on 2021-04-11 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_auto_20210410_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.menu'),
        ),
    ]