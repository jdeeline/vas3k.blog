# Generated by Django 4.1.5 on 2023-01-12 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_alter_comment_options_alter_comment_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="deleted_by",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="is_visible",
        ),
    ]
