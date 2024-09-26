# Generated by Django 3.0.4 on 2020-03-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=1024)),
                ('car_model', models.CharField(max_length=1024)),
                ('color', models.CharField(max_length=1024)),
                ('gov_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=1024)),
                ('lastname', models.CharField(max_length=1024)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DrivingLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.IntegerField()),
                ('starting_date', models.DateField()),
                ('typelevel', models.CharField(choices=[('1', 'First type'), ('2', 'Second type'), ('3', 'Third type')], default=1, max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpd.CarOwner')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpd.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpd.CarOwner')),
            ],
            options={
                'unique_together': {('owner', 'car')},
            },
        ),
    ]
