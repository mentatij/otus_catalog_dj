from django.urls import path

from .views import CategoryDetailView, ProductDetailView, redirect_to_base_category


urlpatterns = [
    path('', redirect_to_base_category),
    path('category/', redirect_to_base_category),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_url'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product_url'),
]
