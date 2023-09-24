# Generated by Django 4.2.5 on 2023-09-24 09:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0002_family1399_family1400"),
    ]

    operations = [
        migrations.AlterField(
            model_name="family1399",
            name="MembersID",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveBigIntegerField(),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="family1400",
            name="MembersID",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveBigIntegerField(),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
