from django.db import models


class Reviews(models.Model):
    image = models.ImageField(upload_to='reviews_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

