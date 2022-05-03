from decimal import Decimal
from django.conf import settings
from shop.models import Product
from cupouns.models import Cupoun


class Cart(object):
    def __init__(self, request):
        # User Cart Initialization
        self.session = request.session
        self.cupoun_id = self.session.get('cupoun_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save the user's cart to the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Adding an item to a user's shopping cart or updating the quantity of an item
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Saving data to session 
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Indicate that the session has been changed
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Iterate over products
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # Number of goods
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def cupoun(self):
        if self.cupoun_id:
            return Cupoun.objects.get(id=self.cupoun_id)
        return None

    def get_discount(self):
        if self.cupoun:
            return (self.cupoun.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()     
