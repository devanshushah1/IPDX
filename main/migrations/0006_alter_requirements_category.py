# Generated by Django 4.0.4 on 2022-05-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_initial_count_requirements_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='category',
            field=models.CharField(blank=True, choices=[('Medicine', 'Medicine'), ('Food', 'Food'), ('Clothing', 'Clothing'), ('Stationary', 'Stationary')], max_length=20, null=True),
        ),
    ]