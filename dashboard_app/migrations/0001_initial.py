# Generated by Django 5.1.1 on 2024-09-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Search",
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
                (
                    "artist_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("search_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]