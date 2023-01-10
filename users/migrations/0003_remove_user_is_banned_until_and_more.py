# Generated by Django 4.1.4 on 2023-01-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_full_name_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_banned_until",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_email_unsubscribed",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_email_verified",
        ),
        migrations.RemoveField(
            model_name="user",
            name="patreon_id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="user",
            name="telegram_data",
        ),
        migrations.RemoveField(
            model_name="user",
            name="telegram_id",
        ),
        migrations.AddField(
            model_name="user",
            name="is_banned",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
