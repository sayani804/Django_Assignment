# Generated by Django 3.2.9 on 2022-01-08 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('student_class', models.IntegerField()),
                ('school', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('rollNo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.studentinfo')),
            ],
        ),
    ]
