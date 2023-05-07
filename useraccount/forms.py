from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from useraccount.models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=('email',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUserModel
        fields=('email',)