# Generated by Django 4.1.3 on 2024-02-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTabs', '0015_formdataentry_delete_formdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_keys', models.CharField(default='empty', max_length=100)),
                ('field_name', models.CharField(default='value', max_length=255)),
                ('selectoption', models.CharField(default='value', max_length=100)),
                ('required', models.BooleanField(default=False)),
                ('readable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_key', models.CharField(default='empty', max_length=100)),
                ('forms_name', models.CharField(default='value', max_length=255)),
                ('Rediretpath_name', models.CharField(default='value', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='FormDataEntry',
        ),
    ]
