# Generated by Django 3.0.2 on 2020-01-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0011_trim_bugsystem_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcasestatus',
            name='id',
            field=models.AutoField(db_column='case_status_id', primary_key=True, serialize=False),
        ),
    ]
