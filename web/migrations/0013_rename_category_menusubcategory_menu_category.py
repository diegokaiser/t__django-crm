# Generated by Django 5.0.4 on 2024-04-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_rename_account_currency_bankaccount_currency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menusubcategory',
            old_name='category',
            new_name='menu_category',
        ),
    ]
