# Generated by Django 3.2.9 on 2022-01-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentacademics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentacademics',
            name='address',
        ),
        migrations.RemoveField(
            model_name='studentacademics',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='studentacademics',
            name='name',
        ),
        migrations.RemoveField(
            model_name='studentacademics',
            name='school',
        ),
        migrations.RemoveField(
            model_name='studentacademics',
            name='student_class',
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='biology',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='chemistry',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='english',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='maths',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='physics',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
