# Generated by Django 4.2 on 2023-06-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_alter_answer_answer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='ai_res_accepted',
            field=models.BooleanField(default=False),
        ),
    ]