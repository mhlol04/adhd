# Generated by Django 5.0.1 on 2024-03-24 21:16

import django.db.models.deletion
import doctors.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("specialize", models.CharField(max_length=100)),
                ("contact", models.IntegerField()),
                ("address", models.CharField(max_length=250)),
                ("experiance", models.IntegerField()),
                ("birth_date", models.DateField()),
                ("photo", models.ImageField(upload_to=doctors.models.upload_photo)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
