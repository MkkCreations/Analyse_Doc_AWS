# Generated by Django 4.2 on 2023-05-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='docType',
            field=models.CharField(max_length=32, null=True),
        ),
    ]