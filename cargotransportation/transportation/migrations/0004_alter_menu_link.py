# Generated by Django 4.2.7 on 2023-12-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0003_alter_menu_options_alter_menu_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(max_length=255, verbose_name='Ссылка'),
        ),
    ]
