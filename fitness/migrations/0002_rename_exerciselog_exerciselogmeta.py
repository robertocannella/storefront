# Generated by Django 5.0.6 on 2024-07-13 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExerciseLog',
            new_name='ExerciseLogMeta',
        ),
    ]