from django.db import models

class Types(models.Model):
    types_name = models.CharField(max_length=50, verbose_name='Тип Лоту')

    class Meta:
        verbose_name= "Тип Лоту"
        verbose_name_plural = "Тип Лоту"
        ordering = ['types_name',]



class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Статус')

    class Meta:
        verbose_name= "Статус"
        verbose_name_plural = "Статус"
        ordering = ['status_name',]



class Сategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категорія')

    class Meta:
        verbose_name= "Категорія"
        verbose_name_plural = "Категорія"
        ordering = ['category_name',]


class Lot(models.Model):
    lot_name = models.CharField(max_length=50, verbose_name='Лот')
    types = models.ForeignKey(Types,on_delete=models.CASCADE, null=True)
    #types = models.ForeignKey('Types',on_delete=models.PROTECT, null=True, to_field='types_name')
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True)
    lot_price = models.DecimalField(max_digits=10, decimal_places=3)
    lot_quantity = models.ImageField()
    category = models.ForeignKey(Сategory,on_delete=models.CASCADE, null=True)
    lot_comment = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name= "Лот"
        verbose_name_plural = "Лот"
        ordering = ['lot_name',]
