# Generated by Django 5.0.6 on 2024-06-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apm_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ashpenser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='ashpenser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]