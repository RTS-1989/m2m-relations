# Generated by Django 2.2.10 on 2020-10-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201011_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagarticle',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]