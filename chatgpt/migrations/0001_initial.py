# Generated by Django 5.0.6 on 2024-06-12 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("thumbnail", models.CharField(max_length=10)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("user_id", models.CharField(default="admin", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ChatRoom",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="EmbeddingFulltextSearchContent",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("c0", models.TextField()),
                ("string_value", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="QA",
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
                ("category", models.CharField(max_length=100)),
                ("qa", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("user_id", models.CharField(default="1", max_length=255)),
                ("user", models.CharField(max_length=255)),
                ("text", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chatgpt.chat"
                    ),
                ),
            ],
        ),
    ]
