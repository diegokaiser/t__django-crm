# Generated by Django 5.0.4 on 2024-04-20 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_bankaccount_account_currency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsystem',
            old_name='idSystem',
            new_name='system',
        ),
        migrations.RemoveField(
            model_name='subsystem',
            name='idSubsystem',
        ),
        migrations.RemoveField(
            model_name='system',
            name='idSystem',
        ),
    ]