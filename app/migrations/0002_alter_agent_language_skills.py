# Generated by Django 5.0.4 on 2024-09-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="language_skills",
            field=models.JSONField(default=list),
        ),
    ]
