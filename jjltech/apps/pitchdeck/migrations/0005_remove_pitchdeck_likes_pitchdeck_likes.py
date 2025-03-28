# Generated by Django 5.1.7 on 2025-03-28 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pitchdeck", "0004_alter_pitchdeck_pitch"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pitchdeck",
            name="likes",
        ),
        migrations.AddField(
            model_name="pitchdeck",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_pitches", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
