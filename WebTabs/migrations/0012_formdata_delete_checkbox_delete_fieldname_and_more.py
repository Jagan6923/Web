# Generated by Django 4.1.3 on 2024-02-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTabs', '0011_checkbox_fieldname_selectionbox_delete_formdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('selection_box', models.CharField(max_length=100)),
                ('is_required', models.BooleanField(default=False)),
                ('is_readable', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='CheckBox',
        ),
        migrations.DeleteModel(
            name='FieldName',
        ),
        migrations.DeleteModel(
            name='SelectionBox',
        ),
    ]
