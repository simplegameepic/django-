# Generated by Django 3.2 on 2022-09-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_remove_quizz_quiz_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='quiz_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
