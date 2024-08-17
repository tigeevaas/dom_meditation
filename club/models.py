from django.db import models


class Schedule(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    date = models.TextField(verbose_name='Дата эфира (1 августа, четверг)')
    time = models.TimeField(verbose_name='Время проведения эфира')

    class Meta:
        db_table = 'schedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return self.name