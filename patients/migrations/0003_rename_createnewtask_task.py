# Generated by Django 5.0.1 on 2024-02-13 18:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0002_createnewtask"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CreateNewTask",
            new_name="Task",
        ),
    ]
