from django.db import models

# Create your models here.
class Record(models.Model):
    heading = models.CharField(max_length=100, verbose_name="Заголовок")
    main_info = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='record/', verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True)
    publication_attribute = models.BooleanField(verbose_name="Признак")
    viewers = models.IntegerField(verbose_name="кол-во просмотров")

    def __str__(self):
        return f"{self.heading}"


    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['heading', ]



