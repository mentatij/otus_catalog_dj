from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    parent_category = models.ForeignKey(
        'self', blank=True, null=True, related_name='subcategories', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        full_title = [self.title]
        parent = self.parent_category
        while parent:
            full_title.append(parent.title)
            parent = parent.parent_category
        return ' -> '.join(full_title[::-1])


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = HTMLField(blank=True)
    full_description = HTMLField(blank=True)
    category = models.ForeignKey(
        'Category', blank=True, null=True, related_name='category_items', on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
