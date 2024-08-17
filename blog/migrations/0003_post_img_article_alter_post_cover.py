# Generated by Django 5.0.6 on 2024-08-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover_alter_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_article',
            field=models.ImageField(blank=True, null=True, upload_to='article_images', verbose_name='Картинка в статью'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images', verbose_name='Картинка на обложку'),
        ),
    ]