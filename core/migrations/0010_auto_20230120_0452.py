# Generated by Django 3.1.3 on 2023-01-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230120_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='time',
            field=models.TimeField(),
        ),
    ]
