# Generated by Django 4.1.3 on 2024-02-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTabs', '0019_checkboxdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkboxdata',
            old_name='field_key',
            new_name='readable_key',
        ),
        migrations.RenameField(
            model_name='checkboxdata',
            old_name='readable',
            new_name='readable_value',
        ),
        migrations.RenameField(
            model_name='checkboxdata',
            old_name='required',
            new_name='required_value',
        ),
        migrations.AddField(
            model_name='checkboxdata',
            name='required_key',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
