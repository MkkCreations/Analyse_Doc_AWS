# Generated by Django 4.2 on 2023-05-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_question_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='alias',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
