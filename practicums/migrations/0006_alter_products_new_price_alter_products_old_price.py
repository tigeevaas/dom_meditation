# Generated by Django 5.0.6 on 2024-07-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicums', '0005_alter_products_options_products_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Новая цена'),
        ),
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Cтарая цена'),
        ),
    ]