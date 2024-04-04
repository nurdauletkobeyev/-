from django.db import models

class Book(models.Model):
    name = models.CharField("Название", max_length=90)
    description = models.TextField("Описание")
    image = models.CharField("Ссылка", max_length=500)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name
