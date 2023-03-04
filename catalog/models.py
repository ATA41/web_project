from django.db import models


class ModelCategory(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Наименование категории")

    def __str__(self):
        return self.category_name


class ModelProduct(models.Model):
    model_name = models.CharField(max_length=255, verbose_name="Наименование модели")
    price = models.IntegerField(verbose_name="Цена")
    category = models.ForeignKey(ModelCategory, on_delete=models.CASCADE, verbose_name="Категория")
    buy = models.BooleanField(verbose_name="Куплено")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="Дата")

    def __str__(self):
        return self.model_name

