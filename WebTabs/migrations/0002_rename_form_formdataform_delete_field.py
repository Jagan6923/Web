# Generated by Django 4.1.3 on 2024-02-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebTabs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form',
            new_name='FormDataForm',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
    ]
