# Generated by Django 3.1.3 on 2023-01-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230120_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
