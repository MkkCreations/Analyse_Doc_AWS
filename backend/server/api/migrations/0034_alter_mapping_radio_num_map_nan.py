# Generated by Django 4.2 on 2023-05-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_mapping_checkbox_mapping_radio_mapping_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping_radio',
            name='num_map_nan',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]
