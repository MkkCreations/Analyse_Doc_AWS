# Generated by Django 4.2 on 2023-05-27 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_rename_diligence_id_document_diligence_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='alias',
        ),
    ]
