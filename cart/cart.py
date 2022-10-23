class Cart:
    '''
    A base Cart class, providing some default behaviors that
    can be inherited or overrided as necessary.
    '''
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}
        self.cart = cart