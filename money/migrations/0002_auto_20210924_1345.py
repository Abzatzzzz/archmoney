# Generated by Django 3.2.5 on 2021-09-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("money", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="depcategory",
            old_name="username",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="deposit",
            old_name="username",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="withcategory",
            old_name="username",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="withdraw",
            old_name="username",
            new_name="user",
        ),
    ]
