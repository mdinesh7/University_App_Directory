# Generated by Django 4.2.6 on 2023-10-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_manager", "0003_alter_app_info_logo_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app_info",
            name="logo_url",
            field=models.ImageField(
                default="/Users/dineshmurugesan/Documents/UniPitt_project/projects/app_directory/media/pics/Canvas.jpeg",
                upload_to="pics",
            ),
        ),
    ]