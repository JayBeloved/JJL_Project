# Generated by Django 5.1.7 on 2025-03-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_profile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, upload_to="profile_pics/"),
        ),
    ]
