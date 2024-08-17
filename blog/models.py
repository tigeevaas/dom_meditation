from django.db import models
from django.utils import timezone
from django_prose_editor.sanitized import SanitizedProseEditorField

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body1 = SanitizedProseEditorField()
    body2 = SanitizedProseEditorField(null=True, blank=True)
    publish = models.DateField(default=timezone.now)
    cover = models.ImageField(upload_to='cover_images', blank=True, null=True, verbose_name='Картинка на обложку')
    img_article = models.ImageField(upload_to='article_images', blank=True, null=True, verbose_name='Картинка в статью')

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title