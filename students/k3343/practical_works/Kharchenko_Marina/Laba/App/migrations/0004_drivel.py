# Generated by Django 3.0.7 on 2020-06-19 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200619_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('comment_type', models.CharField(choices=[('T1', 'Cтарого образца'), ('T2', 'Нового образца'), ('T3', 'Самого новго образца')], max_length=2, null=True)),
                ('Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Owner_d', to='App.Owner')),
            ],
        ),
    ]
