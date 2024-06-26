# Generated by Django 5.0.4 on 2024-04-19 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_brand_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('symbol', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=140)),
                ('bank_name', models.CharField(max_length=140)),
                ('account_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.currencytype')),
            ],
        ),
    ]
