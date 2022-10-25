from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import UserLoginForm, PasswordEmailForm, PasswordResetConfirmForm
from . import views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='customers/register/login.html',
            form_class=UserLoginForm
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/customer/login/'),
        name='logout'
    ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='customers/user/password_reset_form.html',
            success_url='password_reset_email_confirm',
            email_template_name='customers/user/password_reset_email.html',
            form_class=PasswordEmailForm
        ),
        name='pwdreset'
    ),
    path(
        'password-reset-confirm/<slug:uidb64>/<slug:token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='customers/user/password_reset_confirm.html',
            success_url='/customer/password_reset_complete/', 
            form_class=PasswordResetConfirmForm
        ),
        name='password_reset_email_confirm'

    ),
    path(
        'password_reset/password-reset-email-confirm/',
        TemplateView.as_view(template_name="customers/user/reset_status.html"),
        name='password_reset_done'
    ),
    path(
        'password_reset_complete/',
         TemplateView.as_view(template_name="customers/user/reset_status.html"),
         name='password_reset_complete'
    ),
    path('register/', views.register, name="register"),
    path('<slug:uidb64>/<slug:token>/', views.activate, name="activate"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('edit/', views.edit_details, name='edit_details'),
    path('dashboard/delete_user/', views.delete_user, name='delete_user'),
    path(
        'dashboard/delete_confirm/',
        TemplateView.as_view(template_name="customers/user/delete_confirm.html"),
        name='delete_confirmation'
    ),
]
