# Generated by Django 3.1.7 on 2021-03-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_content_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
    ]