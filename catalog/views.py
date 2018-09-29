from django.views.generic import DetailView
from django.shortcuts import redirect

from .models import Product, Category


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/products_list.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


def redirect_to_base_category(request):
    base_page = Category.objects.get(slug='main')
    return redirect(base_page)
