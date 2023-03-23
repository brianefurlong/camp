# Generated by Django 4.1.7 on 2023-03-22 17:43

import django.db.models.deletion
import rules.contrib.models
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0003_alter_game_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ruleset",
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
                ("package", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rulesets",
                        to="game.game",
                    ),
                ),
            ],
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]
