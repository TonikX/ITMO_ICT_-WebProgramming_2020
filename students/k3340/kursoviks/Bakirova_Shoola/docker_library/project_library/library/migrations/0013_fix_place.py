# Generated by Django 2.0.6 on 2020-10-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20201027_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='fix',
            name='place',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='place_fix', to='library.Place', verbose_name='Место чтения'),
            preserve_default=False,
        ),
    ]
