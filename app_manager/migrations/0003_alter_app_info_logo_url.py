# Generated by Django 4.2.6 on 2023-10-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_manager", "0002_app_info_is_free"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app_info",
            name="logo_url",
            field=models.ImageField(default=None, upload_to="pics"),
        ),
    ]
