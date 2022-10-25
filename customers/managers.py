from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **etc):
        if not email:
            raise ValueError(_('User must have an email'))
        if not password:
            raise ValueError("Users must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email, **etc)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **etc):
        etc.setdefault('is_staff', True)
        etc.setdefault('is_superuser', True)
        etc.setdefault('is_active', True)

        if etc.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff= True.'))

        if etc.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser= True.'))

        return self.create_user(email, password, **etc)
