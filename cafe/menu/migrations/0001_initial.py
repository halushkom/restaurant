# Generated by Django 3.0.4 on 2020-05-20 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва категорії')),
                ('slug', models.SlugField(max_length=150, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, null=True, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Назва бляда')),
                ('description', models.TextField(null=True, verbose_name='Опис страви')),
                ('price', models.CharField(max_length=150, null=True, verbose_name='Ціна')),
                ('image', models.ImageField(null=True, upload_to='static/', verbose_name='Зображення страви')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Category', verbose_name='Вибір категорії')),
            ],
            options={
                'verbose_name_plural': 'Меню',
            },
        ),
    ]