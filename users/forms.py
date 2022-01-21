from django.contrib.auth.forms import UserChangeForm, UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from django.forms import Form, ModelForm


User = get_user_model()

class UserCreationForm(BaseUserCreationForm):

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('email', "username", 'first_name', 'last_name', 'country', 'favorite_category')
        


class UserProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'favorite_category')
        #field_classes = {'username': UsernameField}