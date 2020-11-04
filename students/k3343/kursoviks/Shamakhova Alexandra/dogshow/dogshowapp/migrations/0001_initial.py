# Generated by Django 3.1.2 on 2020-11-03 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_club', models.CharField(max_length=20, null=True, verbose_name='Клуб')),
                ('dog_name', models.CharField(max_length=20, verbose_name='Кличка')),
                ('dog_breed', models.CharField(max_length=20, verbose_name='Порода')),
                ('dog_age', models.CharField(max_length=10, verbose_name='Возраст')),
                ('dog_class', models.CharField(choices=[('Э', 'Элита'), ('I', 'Первый племенной класс'), ('II', 'Второй племенной класс'), ('III', 'Третий племенной класс')], max_length=3, verbose_name='Классность')),
                ('dog_document', models.CharField(max_length=20, verbose_name='Номер документа')),
                ('dog_mother', models.CharField(max_length=20, verbose_name='Кличка матери')),
                ('dog_father', models.CharField(max_length=20, verbose_name='Кличка отца')),
                ('dog_vaccination', models.DateField(verbose_name='Дата последней прививки')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
        migrations.CreateModel(
            name='Experts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_surname', models.CharField(max_length=20, verbose_name='Фамилия эксперта')),
                ('expert_name', models.CharField(max_length=20, verbose_name='Имя эксперта')),
                ('expert_club', models.CharField(max_length=20, verbose_name='Клуб эксперта')),
            ],
            options={
                'verbose_name': 'Эксперт',
                'verbose_name_plural': 'Эксперты',
            },
        ),
        migrations.CreateModel(
            name='Funders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funder_name', models.CharField(max_length=20, verbose_name='ФИО или компания')),
            ],
            options={
                'verbose_name': 'Спонсор',
                'verbose_name_plural': 'Спонсоры',
            },
        ),
        migrations.CreateModel(
            name='Rings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ring_number', models.CharField(max_length=10, verbose_name='Номер ринга')),
            ],
            options={
                'verbose_name': 'Ринг',
                'verbose_name_plural': 'Ринги',
            },
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_presentment', models.CharField(max_length=20, verbose_name='Описание выставки')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_funder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.funders')),
                ('sponsor_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.shows')),
            ],
            options={
                'verbose_name': 'Спонсирование',
                'verbose_name_plural': 'Спонсирования',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_medical', models.BooleanField(default=False, verbose_name='медосмотр')),
                ('record_pay', models.BooleanField(default=False, verbose_name='оплата счёта')),
                ('record_confirmation', models.BooleanField(default=False, verbose_name='Подтверждение')),
                ('record_dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.dogs')),
                ('record_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.shows')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Judgings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judging_confirmation', models.BooleanField(default=False, verbose_name='Подтверждение')),
                ('judging_expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.experts')),
                ('judging_ring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.rings')),
                ('judging_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.shows')),
            ],
            options={
                'verbose_name': 'Судейство',
                'verbose_name_plural': 'Судейства',
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('human_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('human_patronym', models.CharField(max_length=20, verbose_name='Отчество')),
                ('human_passport', models.CharField(max_length=10, verbose_name='Паспорт')),
                ('org', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dogs',
            name='dog_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.human'),
        ),
        migrations.CreateModel(
            name='Acts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_1', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='упражнение 1')),
                ('act_2', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='упражнение 2')),
                ('act_3', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='упражнение 3')),
                ('act_dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.dogs')),
                ('act_ring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.rings')),
                ('act_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshowapp.shows')),
            ],
            options={
                'verbose_name': 'Выступление',
                'verbose_name_plural': 'Выступления',
            },
        ),
    ]
