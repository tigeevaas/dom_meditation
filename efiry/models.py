from django.db import models


class Efir(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
    all_description = models.TextField(blank=True, null=True, verbose_name='Полное описание')
    duration = models.TimeField()
    image = models.ImageField(upload_to='meditations_images', blank=True, null=True, verbose_name='Изображение')
    old_price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Cтарая цена')
    new_price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Новая цена')
    link = models.TextField(blank=True, null=True, verbose_name='id для модального окна (с #)')
    id_modal = models.TextField(blank=True, null=True, verbose_name='id для модального окна (без #)')
    link_web = models.TextField(blank=True, null=True, verbose_name='Ссылка на сайт')

    class Meta:
        db_table = 'efiry'
        verbose_name = 'Эфир'
        verbose_name_plural = 'Эфиры'

    def __str__(self):
        return self.name
