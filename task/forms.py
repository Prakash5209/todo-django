from django import forms

from task.models import Task

class Task_form(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','description')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'title'})
        # self.fields['description'].widget.attrs.update({'class':'form-control','rows':5,'placeholder':'description'})
        # self.fields['description'].widget.attrs.update({'rows':5})
        
        for field in self.fields:
            if field=='description':
                self.fields[field].widget.attrs.update({'rows':5})
            self.fields[field].widget.attrs.update({'placeholder':f'{field}','class':'form-control'})
            # print(type(field))
            
        
        
        