# Generated by Django 3.1.3 on 2023-01-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230120_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='time',
            field=models.TimeField(),
        ),
    ]
