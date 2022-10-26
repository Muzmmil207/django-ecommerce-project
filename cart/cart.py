from products.models import Product


class Cart:
    """
    A base Cart class, providing some default behaviors that
    can be inherited or overrided as necessary.
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if cart == None:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = item['price'] * item['qty']
        yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())

    def save(self):
        self.session.modified = True
        
    def get_cart_total(self):
        return sum(item['price'] * item['qty'] for item in self.cart.values())

    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = product.id

        if product_id in self.cart:
            self.cart[str(product_id)]['qty'] = qty
        else:
            self.cart[str(product_id)] = {'price': float(product.price), 'qty': qty}
        self.save()

    def update(self, product_id, action):
        if product_id in self.cart:
            product =  self.cart[product_id]

            if action == 'plus':
                product['qty'] += 1
            elif action == 'minus':
                product['qty'] -= 1
                if product['qty'] < 0: self.delete(product_id)
            self.save()

    def delete(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

