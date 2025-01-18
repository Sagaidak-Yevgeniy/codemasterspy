from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    image = models.ImageField(upload_to="course_images/", verbose_name="Изображение курса")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность курса")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена курса")

    def __str__(self):
        return self.title