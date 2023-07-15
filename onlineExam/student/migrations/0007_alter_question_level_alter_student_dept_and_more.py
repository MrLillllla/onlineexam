# Generated by Django 4.2.1 on 2023-05-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_alter_question_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="level",
            field=models.CharField(
                choices=[("3", "difficult"), ("2", "general"), ("1", "easy")],
                max_length=10,
                verbose_name="等级",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="dept",
            field=models.CharField(
                choices=[
                    ("教育学部", "教育学部"),
                    ("心理学院", "心理学院"),
                    ("政法学院", "政法学院"),
                    ("经济与管理学院", "经济与管理学院"),
                    ("文学院", "文学院"),
                    ("历史文化学院", "历史文化学院"),
                    ("外国语学院", "外国语学院"),
                    ("音乐学院", "音乐学院"),
                    ("美术学院", "美术学院"),
                    ("马克思主义学部", "马克思主义学部"),
                    ("数学与统计学院", "数学与统计学院"),
                    ("信息科学与技术学院", "信息科学与技术学院"),
                    ("物理学院", "物理学院"),
                    ("化学学院", "化学学院"),
                    ("生命科学学院", "生命科学学院"),
                    ("地理科学学院", "地理科学学院"),
                    ("环境学院", "环境学院"),
                    ("体育学院（冰雪学院）", "体育学院（冰雪学院）"),
                    ("传媒科学学院（新闻学院）", "传媒科学学院（新闻学院）"),
                    ("国际汉学院（海外教育学院）", "国际汉学院（海外教育学院）"),
                    ("东北师范大学罗格斯大学•纽瓦克学院", "东北师范大学罗格斯大学•纽瓦克学院"),
                ],
                default=None,
                max_length=20,
                verbose_name="学院",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="dept",
            field=models.CharField(
                choices=[
                    ("教育学部", "教育学部"),
                    ("心理学院", "心理学院"),
                    ("政法学院", "政法学院"),
                    ("经济与管理学院", "经济与管理学院"),
                    ("文学院", "文学院"),
                    ("历史文化学院", "历史文化学院"),
                    ("外国语学院", "外国语学院"),
                    ("音乐学院", "音乐学院"),
                    ("美术学院", "美术学院"),
                    ("马克思主义学部", "马克思主义学部"),
                    ("数学与统计学院", "数学与统计学院"),
                    ("信息科学与技术学院", "信息科学与技术学院"),
                    ("物理学院", "物理学院"),
                    ("化学学院", "化学学院"),
                    ("生命科学学院", "生命科学学院"),
                    ("地理科学学院", "地理科学学院"),
                    ("环境学院", "环境学院"),
                    ("体育学院（冰雪学院）", "体育学院（冰雪学院）"),
                    ("传媒科学学院（新闻学院）", "传媒科学学院（新闻学院）"),
                    ("国际汉学院（海外教育学院）", "国际汉学院（海外教育学院）"),
                    ("东北师范大学罗格斯大学•纽瓦克学院", "东北师范大学罗格斯大学•纽瓦克学院"),
                ],
                default=None,
                max_length=20,
                verbose_name="学院",
            ),
        ),
    ]