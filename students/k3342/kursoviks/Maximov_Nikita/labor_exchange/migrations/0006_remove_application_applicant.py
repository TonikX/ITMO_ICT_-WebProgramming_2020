# Generated by Django 3.0 on 2020-10-06 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labor_exchange', '0005_vacancy_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
    ]
