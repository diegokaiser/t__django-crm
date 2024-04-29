# Generated by Django 5.0.4 on 2024-04-19 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_currencytype_jobtitle_paymentmethod_tipovia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reason',
            name='icon',
            field=models.FileField(upload_to='reasons/icons', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]),
        ),
    ]
