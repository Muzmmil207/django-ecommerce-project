from functools import wraps
from django.shortcuts import redirect


def is_not_authenticated(function):
    @wraps(function)
    def wrap(request, *args):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return function(request, *args)

    return wrap

