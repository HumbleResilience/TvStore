from django.shortcuts import render, get_object_or_404, redirect
from django_countries import override
from .shoppingcart import Cart
from cart.models import Product
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart= Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd= form.cleaned_data
        cart.add(product=product, quanity=cd['quanity'], override_quanity=cd['override'])
    return redirect ('shoppingcart:cart_detail')

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shoppingcart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quanity_form'] = CartAddProductForm(initial={'quanity':item['quanity'], 'override':True})
    return redirect(request, 'cart:detail.html', {'cart':cart})
