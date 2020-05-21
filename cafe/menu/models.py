from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=150)
    slug = models.SlugField('URL', max_length=150, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.slug})
    class Meta:
        verbose_name_plural = 'Категорії'


class Meal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Вибір категорії')
    slug = models.SlugField('URL', max_length=150, null=True, unique=True)
    name = models.CharField('Назва блюда', null=True, max_length=150)
    description = models.TextField('Опис страви', null=True)
    price = models.CharField("Ціна", null=True, max_length=150)
    image = models.ImageField('Зображення страви', upload_to='static/', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Меню'
