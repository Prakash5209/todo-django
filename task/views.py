from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from task.models import Task
from task.forms import Task_form

# class TaskClassView(ListView):
#     template_name='task.html'
#     model=Task
    # def get_queryset(self,**kwargs):
    #     return super().get_queryset(**kwargs).filter(user = self.request.user)
    
@login_required
def TaskClassView(request):
    left_to_do_task = len(Task.objects.filter(is_completed = False,user = request.user))
    total_task = len(Task.objects.filter(user = request.user))
    completed_task = len(Task.objects.filter(is_completed = True, user = request.user))
    vari = Task.objects.filter(user = request.user) if request.user.is_authenticated else None
    form = Task_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.add_message(request,messages.SUCCESS,'new task added')
        return redirect('task:TaskClassView')
    context = {'object_list':vari,'form':form,'left_to_do_task':left_to_do_task,'completed_task':completed_task,'total_task':total_task}
    return render(request,'task.html',context)
    
# @login_required
# def new_task(request):
#     form = Task_form(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = request.user
#         obj.save()
#         return redirect('task:TaskClassView')
#     context={'form':form}
#     return render(request,'form.html',context)

def delete_task(request,pk):
    task_model=Task.objects.get(id = pk,user = request.user)
    if request.method == "POST":
        task_model.delete()
        messages.add_message(request,messages.INFO,'task deleted or canceled')
        return redirect('task:TaskClassView')
    return render(request,'delete_task.html',{'task_model':task_model})
    
def edit_task(request,pk):
    task_model = Task.objects.get(id=pk,user = request.user)
    form = Task_form(request.POST or None, instance=task_model)
    if request.method == 'POST':
        form.save()
        messages.add_message(request,messages.SUCCESS,'task updated')
        return redirect('task:TaskClassView')
    context={'form':form}
    return render(request,'task.html',context)

def toggle(request,pk):
    task_model = Task.objects.get(id = pk)
    if task_model.is_completed == True:
        task_model.is_completed = False
        task_model.save()
        return redirect('task:TaskClassView')
    else:
        task_model.is_completed = True
        task_model.save()
        return redirect('task:TaskClassView')
