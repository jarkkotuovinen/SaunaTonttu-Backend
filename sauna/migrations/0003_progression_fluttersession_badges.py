# Generated by Django 4.1.1 on 2024-04-22 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sauna", "0002_saunasession_avg_humid_saunasession_avg_pressure_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Progression",
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
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("level", models.IntegerField()),
                ("streak", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FlutterSession",
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
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("start_time", models.DateTimeField()),
                (
                    "duration",
                    models.DecimalField(
                        decimal_places=4, default=0.0, editable=False, max_digits=10
                    ),
                ),
                (
                    "avg_temp",
                    models.DecimalField(
                        decimal_places=4, default=0.0, editable=False, max_digits=10
                    ),
                ),
                (
                    "avg_humid",
                    models.DecimalField(
                        decimal_places=4, default=0.0, editable=False, max_digits=10
                    ),
                ),
                (
                    "avg_pressure",
                    models.DecimalField(
                        decimal_places=4, default=0.0, editable=False, max_digits=10
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Badges",
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
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("badgeID", models.IntegerField()),
                (
                    "progression",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sauna.progression",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]