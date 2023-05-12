from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from task.models import Task
from task.forms import Task_form

# class TaskClassView(ListView):
#     template_name='task.html'
#     model=Task
    # def get_queryset(self,**kwargs):
    #     return super().get_queryset(**kwargs).filter(user = self.request.user)
    
def TaskClassView(request):
    # vari = Task.objects.all()
    vari = Task.objects.filter(user = request.user) if request.user.is_authenticated else None
    context = {'object_list':vari}
    return render(request,'task.html',context)
    
@login_required
def new_task(request):
    form = Task_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('task:TaskClassView')
    context={'form':form}
    return render(request,'form.html',context)

def delete_task(request,pk):
    task_model=Task.objects.get(id = pk)
    task_model.delete()
    return redirect('task:TaskClassView')

def edit_task(request,pk):
    task_model = Task.objects.get(id=pk)
    form = Task_form(request.POST or None, instance=task_model)
    if request.method == 'POST':
        form.save()
        return redirect('task:TaskClassView')
    context={'form':form}
    return render(request,'form.html',context)
