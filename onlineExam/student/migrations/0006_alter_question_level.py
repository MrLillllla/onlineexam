# Generated by Django 4.2.1 on 2023-05-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0005_auto_20190609_1914"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="level",
            field=models.CharField(
                choices=[("3", "difficult"), ("1", "easy"), ("2", "general")],
                max_length=10,
                verbose_name="等级",
            ),
        ),
    ]