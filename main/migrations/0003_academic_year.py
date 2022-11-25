# Generated by Django 4.1.3 on 2022-11-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]