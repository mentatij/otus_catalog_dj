from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from tinymce.models import HTMLField


def create_slug(title):
    new_slug = slugify(title)
    return new_slug + '-' + str(int(time()))


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

    def get_absolute_url(self):
        return reverse('category_url', args=(self.slug,))


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/', default='images/no-img.png')
    short_description = HTMLField(blank=True)
    full_description = HTMLField(blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        'Category', blank=True, null=True, related_name='category_items', on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = create_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_url', args=(self.slug,))
