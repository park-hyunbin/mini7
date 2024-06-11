# Generated by Django 5.0.6 on 2024-06-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("chatgpt", "0003_delete_chromadata_delete_history"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("query", models.CharField(max_length=255)),
                ("answer", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("sim1", models.FloatField()),
                ("sim2", models.FloatField()),
                ("sim3", models.FloatField()),
            ],
        ),
    ]