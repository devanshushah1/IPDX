# Generated by Django 4.0.4 on 2022-05-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_ngo_aim_ngo_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='aim',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]