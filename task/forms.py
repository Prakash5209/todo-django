from django import forms

from task.models import Task

class Task_form(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','description')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['description'].widget.attrs.update({'rows':3})
        
        
        