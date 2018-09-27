from django.views.generic import DetailView, ListView


class ProductDetailView(DetailView):
    model = 'Product'
    template_name = 'product_detail.html'
