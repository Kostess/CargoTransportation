# Generated by Django 4.2.7 on 2023-12-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_alter_menu_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('short_description', models.CharField(blank=True, max_length=255, verbose_name='Краткое описание')),
                ('full_description', models.TextField(blank=True, verbose_name='Полное описание')),
                ('image_card', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Карточка закоза',
                'verbose_name_plural': 'Карточки закозов',
            },
        ),
    ]
