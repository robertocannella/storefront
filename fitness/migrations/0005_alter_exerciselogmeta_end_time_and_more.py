# Generated by Django 5.0.6 on 2024-07-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_alter_exerciselogmeta_log_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciselogmeta',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='exerciselogmeta',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
