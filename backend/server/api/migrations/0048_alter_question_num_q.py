# Generated by Django 4.2 on 2023-06-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_alter_mapping_radio_num_map_nan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='num_q',
            field=models.CharField(max_length=32),
        ),
    ]
