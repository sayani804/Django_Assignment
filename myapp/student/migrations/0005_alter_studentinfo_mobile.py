# Generated by Django 3.2.9 on 2022-01-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20220108_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]