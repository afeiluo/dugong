# Generated by Django 3.2.9 on 2021-11-27 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0006_remove_photo_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "category",
                "verbose_name_plural": "category",
            },
        ),
    ]
