from django import forms

from task.models import Task

class Task_form(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','description',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }
        