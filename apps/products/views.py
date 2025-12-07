from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm


class ProductOwnerMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Product.objects.all()

    def get_object(self, queryset=None):
        return super().get_object(queryset=self.get_queryset())


class ProductListView(ProductOwnerMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductCreateView(ProductOwnerMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')


class ProductUpdateView(ProductOwnerMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:list')


class ProductDeleteView(ProductOwnerMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:list')