from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField


class StoreProductModel(models.Model):
    name = models.CharField("Название магазина", max_length=40, null=False, blank=False, db_index=True)
    description = models.TextField("Описание магазина", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store", kwargs={"id": self.id})


class CategoryProductModel(models.Model):
    name = models.CharField("Категория продукта", max_length=40, unique=True, null=False, blank=False, db_index=True)
    description = models.TextField("Описание категории", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_product", kwargs={"id": self.id})


class ProductModel(models.Model):
    name = models.CharField("Название продукта", max_length=70, unique=True, null=False, blank=False, db_index=True)
    description = models.TextField("Описание", max_length=255, null=True, blank=True)
    buy = models.BooleanField("Куплен", default=False, help_text="Куплен ли продукт или нет")
    developer = models.CharField("Разработчик", max_length=70, null=True, blank=True)
    category = models.ManyToManyField(CategoryProductModel, blank=True, default=None)
    store_product = models.ManyToManyField(StoreProductModel, blank=True, default=None)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"id": self.id})


class ProductPriceModel(models.Model):
    name = models.CharField("Название магазина", max_length=40, null=False, blank=False, db_index=True)
    price = MoneyField("Цена", max_digits=10, decimal_places=2, default_currency="USD")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("price", kwargs={"id": self.id})
