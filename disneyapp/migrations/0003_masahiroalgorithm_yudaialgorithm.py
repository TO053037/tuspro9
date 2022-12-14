# Generated by Django 4.1.3 on 2022-12-02 05:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disneyapp', '0002_rename_timevisitingallattractions_wadaalgorithm'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasahiroAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visit_all_attractions', models.BooleanField(default=False)),
                ('time', models.IntegerField(default=-1)),
                ('date', models.DateField()),
                ('route', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='YudaiAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visit_all_attractions', models.BooleanField(default=False)),
                ('time', models.IntegerField(default=-1)),
                ('date', models.DateField()),
                ('route', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]
