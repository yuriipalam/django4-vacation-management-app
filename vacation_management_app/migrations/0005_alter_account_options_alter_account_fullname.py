# Generated by Django 4.1.2 on 2022-10-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_management_app', '0004_account_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['status'], 'verbose_name': 'User Status', 'verbose_name_plural': 'User Statuses'},
        ),
        migrations.AlterField(
            model_name='account',
            name='fullname',
            field=models.CharField(max_length=100, verbose_name='Full name'),
        ),
    ]