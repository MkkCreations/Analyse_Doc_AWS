# Generated by Django 4.2 on 2023-05-28 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_mappingcheckbox_mappingradio_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MappingCheckBox',
            new_name='Mapping_checkBox',
        ),
        migrations.RenameModel(
            old_name='MappingRadio',
            new_name='Mapping_radio',
        ),
        migrations.RenameModel(
            old_name='MappingText',
            new_name='Mapping_text',
        ),
    ]
