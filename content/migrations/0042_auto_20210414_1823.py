# Generated by Django 3.1.7 on 2021-04-14 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0041_auto_20210414_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.category'),
        ),
    ]
