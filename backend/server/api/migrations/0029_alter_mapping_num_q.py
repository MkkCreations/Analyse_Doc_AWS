# Generated by Django 4.2 on 2023-05-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_remove_question_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='num_q',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
