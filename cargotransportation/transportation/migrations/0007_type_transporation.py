# Generated by Django 4.2.7 on 2023-12-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0006_alter_cards_orders_image_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_transporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_type', models.CharField(max_length=60, verbose_name='Типы перевозок')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image_type', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Тип перевозок',
                'verbose_name_plural': 'Типы перевозок',
            },
        ),
    ]
