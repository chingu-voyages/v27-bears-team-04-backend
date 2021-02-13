from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where user can login with his email or his username
    """
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("User must have a valid email address"))

        if not kwargs.get('username'):
            raise ValueError('User must have a valid username')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=kwargs.get('username').strip(),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        
        if kwargs.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(email, password, **kwargs)
