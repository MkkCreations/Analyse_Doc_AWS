# Generated by Django 4.2 on 2023-05-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_answer_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping_text',
            name='num_q',
            field=models.CharField(max_length=16),
        ),
    ]