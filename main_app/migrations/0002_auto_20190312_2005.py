# Generated by Django 2.1.5 on 2019-03-12 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealbreaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PriorFlame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('relationship_duration', models.IntegerField()),
                ('breakup_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bachelor',
            name='dealbreaker',
        ),
        migrations.AddField(
            model_name='priorflame',
            name='bachelor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Bachelor'),
        ),
        migrations.AddField(
            model_name='dealbreaker',
            name='bachelor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Bachelor'),
        ),
    ]
