# Generated by Django 3.2.16 on 2023-05-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_productmodel_buy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpricemodel',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='productpricemodel',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]