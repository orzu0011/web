# Generated by Django 5.1 on 2024-08-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(default='57000', max_length=150, unique=True),
        ),
    ]
