# Generated by Django 5.1 on 2024-08-18 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Dars davomiyligi',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('course_code', models.CharField(default='55629', max_length=150, unique=True)),
                ('course_duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('lesson_duration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.lesson_duration')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
    ]
