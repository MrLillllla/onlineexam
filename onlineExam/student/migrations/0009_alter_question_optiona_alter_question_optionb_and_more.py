# Generated by Django 4.2.1 on 2023-05-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0008_alter_question_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="optionA",
            field=models.CharField(max_length=100, verbose_name="A选项"),
        ),
        migrations.AlterField(
            model_name="question",
            name="optionB",
            field=models.CharField(max_length=100, verbose_name="B选项"),
        ),
        migrations.AlterField(
            model_name="question",
            name="optionC",
            field=models.CharField(max_length=100, verbose_name="C选项"),
        ),
        migrations.AlterField(
            model_name="question",
            name="optionD",
            field=models.CharField(max_length=100, verbose_name="D选项"),
        ),
    ]
