# Generated by Django 4.1.5 on 2023-01-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
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
                ("code", models.CharField(max_length=8)),
                ("name", models.CharField(max_length=20)),
                ("hour", models.CharField(max_length=5)),
                ("credits", models.CharField(max_length=10)),
                ("state", models.CharField(max_length=10)),
            ],
        ),
    ]
