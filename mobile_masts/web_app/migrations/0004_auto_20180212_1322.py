# Generated by Django 2.0.1 on 2018-02-12 13:22

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_auto_20180211_1908'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='property',
            managers=[
                ('mast_table', django.db.models.manager.Manager()),
            ],
        ),
    ]
