# Generated by Django 3.0.7 on 2020-06-09 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20200609_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Students', verbose_name='Номер группы'),
        ),
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.CharField(max_length=10, verbose_name='Номер группы'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='class_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер кабинета'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
