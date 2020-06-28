# Generated by Django 3.0.5 on 2020-05-26 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shadule', '0003_auto_20200526_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'ФИО', 'verbose_name_plural': 'ФИО'},
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('type', models.CharField(max_length=50, verbose_name='Тип комментария')),
                ('importance', models.CharField(max_length=50, verbose_name='Важность комментария')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shadule.Homework', verbose_name='Домашнее задание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
