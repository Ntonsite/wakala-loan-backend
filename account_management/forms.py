from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Role


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('roles', 'middle_name')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
