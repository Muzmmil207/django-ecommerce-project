class Cart:
    """
    A base Cart class, providing some default behaviors that
    can be inherited or overrided as necessary.
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = product.id

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': float(product.price), 'qty': qty}

        self.save()

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())


    def save(self):
        self.session.modified = True