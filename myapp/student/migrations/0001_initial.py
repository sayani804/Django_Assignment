# Generated by Django 3.2.9 on 2022-01-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('rollNo', models.IntegerField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('student_class', models.IntegerField()),
                ('school', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
