from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=120)),
                ('wallet', models.IntegerField(default=0)),
                ('token_id', models.CharField(default='91674392', max_length=150, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=256, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('extra_phone', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=256, null=True)),
                ('telegram', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]