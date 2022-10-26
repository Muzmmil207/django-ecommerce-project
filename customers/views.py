from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from customers.models import User
from .token import account_activation_token
from .forms import RegistrationForm, UserEditForm
from .decorators import is_not_authenticated
# Create your views here.

@login_required
def dashboard(request):
    context = {}
    return render(request, 'customers/user/dashboard.html', context)


@login_required
def edit_details(request):
    form = UserEditForm(instance=request.user)

    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'customers/user/edit_details.html', context)


@login_required
def delete_user(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return redirect('delete_confirmation')


@is_not_authenticated 
def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('customers/register/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')

    context = {'form': form}

    return render(request, 'customers/register/registration.html', context)


def activate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(user)
        return redirect('dashboard')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('register')

