# Generated by Django 5.0.6 on 2024-07-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicums', '0010_alter_practicums_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicums',
            name='id_model',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на сайт'),
        ),
    ]