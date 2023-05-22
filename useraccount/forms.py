from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from useraccount.models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=('email',)
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control'})
                
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUserModel
        fields=('email',)