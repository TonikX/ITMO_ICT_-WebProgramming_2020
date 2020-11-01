# Generated by Django 3.1.2 on 2020-11-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_list', '0005_auto_20201101_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_rank',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_text',
            field=models.TextField(max_length=500, verbose_name='Отзыв'),
        ),
    ]
