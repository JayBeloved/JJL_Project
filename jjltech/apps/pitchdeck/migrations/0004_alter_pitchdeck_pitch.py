# Generated by Django 5.1.7 on 2025-03-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "pitchdeck",
            "0003_alter_pitchdeck_facebook_alter_pitchdeck_instagram_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="pitchdeck",
            name="pitch",
            field=models.TextField(max_length=7000),
        ),
    ]
