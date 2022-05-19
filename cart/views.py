
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from shoppingcart.forms import CartAddProductForm

# Create your views here.

def product_list( request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'cart/product/list.html', {'category':category, 'categories':categories, 'products':products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available= True)
    shoppingcart_product_form = CartAddProductForm
    return render(request, 'cart/product/detail.html', {'product':product, 'shoppingcart_product_form':shoppingcart_product_form})