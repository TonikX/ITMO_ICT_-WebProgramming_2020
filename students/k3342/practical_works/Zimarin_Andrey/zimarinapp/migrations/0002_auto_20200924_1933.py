# Generated by Django 2.2 on 2020-09-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zimarinapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='owning',
            name='date_ended',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='owning',
            name='date_started',
            field=models.DateField(blank=True, null=True),
        ),
    ]
