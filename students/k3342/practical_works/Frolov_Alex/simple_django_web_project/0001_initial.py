# Generated by Django 3.0.6 on 2020-05-08 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('mark', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('avto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Avto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('number_license', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_issue', models.DateField()),
                ('category', models.CharField(blank=True, choices=[('A', 'A'), ('A1', 'A1'), ('B', 'B'), ('B1', 'B1'), ('C', 'C')], max_length=2)),
                ('owner_license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
    ]
