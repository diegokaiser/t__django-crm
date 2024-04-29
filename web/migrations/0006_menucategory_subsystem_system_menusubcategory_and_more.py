# Generated by Django 5.0.4 on 2024-04-20 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_bannera_background_alter_bannera_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('idMenuCategory', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subsystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('idSubsystem', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('idSystem', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('idMenuSubcategory', models.PositiveIntegerField()),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.menucategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='idSubsystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.subsystem'),
        ),
        migrations.AddField(
            model_name='subsystem',
            name='idSystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.system'),
        ),
        migrations.AddField(
            model_name='product',
            name='idSystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.system'),
        ),
    ]
