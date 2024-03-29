# Generated by Django 4.1.3 on 2024-02-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebTabs', '0016_fielddata_formdata_delete_formdataentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fielddata',
            old_name='form_keys',
            new_name='field_key',
        ),
        migrations.RenameField(
            model_name='fielddata',
            old_name='field_name',
            new_name='field_value',
        ),
        migrations.RenameField(
            model_name='fielddata',
            old_name='selectoption',
            new_name='selection_value',
        ),
        migrations.RemoveField(
            model_name='fielddata',
            name='readable',
        ),
        migrations.RemoveField(
            model_name='fielddata',
            name='required',
        ),
    ]
