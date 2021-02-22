from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    """
    Personalization of the User creation form to accept email as username
    """
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
        )


class EditProfile(UserChangeForm):
    """
    Allows future users' updates
    """
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
        )
