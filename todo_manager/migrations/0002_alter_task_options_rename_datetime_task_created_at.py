# Generated by Django 4.2.7 on 2023-11-19 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_completed']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='datetime',
            new_name='created_at',
        ),
    ]
