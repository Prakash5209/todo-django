from django.shortcuts import render,redirect
from django.views.generic import ListView

from task.models import Task
from task.forms import Task_form

class TaskClassView(ListView):
    template_name='task.html'
    model=Task
    
def new_task(request):
    form = Task_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task:TaskClassView')
    context={'form':form}
    return render(request,'form.html',context)

def delete_task(request,pk):
    task_model=Task.objects.get(id = pk)
    task_model.delete()
    return redirect('task:TaskClassView')

