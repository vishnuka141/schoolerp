# Generated by Django 4.1.3 on 2022-11-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttype',
            name='fee_type',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]