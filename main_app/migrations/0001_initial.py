# Generated by Django 2.1.5 on 2019-03-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bachelor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('wealth_origin', models.TextField(max_length=250)),
                ('location', models.CharField(max_length=100)),
                ('net_worth', models.IntegerField()),
                ('dealbreaker', models.TextField(max_length=250)),
            ],
        ),
    ]
