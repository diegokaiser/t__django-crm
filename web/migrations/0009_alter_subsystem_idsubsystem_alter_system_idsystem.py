# Generated by Django 5.0.4 on 2024-04-20 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_subsystem_idsubsystem_alter_system_idsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsystem',
            name='idSubsystem',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Solo están permitidos los caracteres alfanuméricos.')]),
        ),
        migrations.AlterField(
            model_name='system',
            name='idSystem',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Solo están permitidos los caracteres alfanuméricos.')]),
        ),
    ]
