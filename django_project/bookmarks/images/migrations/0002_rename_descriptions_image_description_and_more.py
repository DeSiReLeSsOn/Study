# Generated by Django 4.1.10 on 2023-09-07 18:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="descriptions",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="image",
            old_name="user_like",
            new_name="users_like",
        ),
    ]
