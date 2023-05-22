# Generated by Django 4.1.7 on 2023-04-06 20:28

import django.db.models.deletion
import rules.contrib.models
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("game", "0005_alter_chapter_unique_together_ruleset_enabled_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
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
                    "name",
                    models.CharField(
                        help_text="Name of the character.", max_length=255
                    ),
                ),
                (
                    "player_name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the player, if different from the owner. Typically used when managing characters for family members.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "chapter",
                    models.ForeignKey(
                        help_text="The chapter this character belongs to.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="characters",
                        to="game.chapter",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="The user who owns this character. Not necessarily the character's portrayer.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="characters",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Sheet",
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
                    "primary",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this sheet is the primary sheet for the character.",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        help_text="The label to use for this sheet, if it is not the primary sheet. Non-primary sheets are typically medical reforges, build-downs for use in other chapters, test sheets, etc.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="The data for this sheet, in the format expected by the ruleset.",
                    ),
                ),
                (
                    "character",
                    models.ForeignKey(
                        help_text="The character this sheet is for.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sheets",
                        to="character.character",
                    ),
                ),
                (
                    "ruleset",
                    models.ForeignKey(
                        help_text="The ruleset this sheet is intended to use.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sheets",
                        to="game.ruleset",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]