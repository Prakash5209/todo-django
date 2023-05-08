from django.urls import path

from task.views import TaskClassView,new_task,delete_task,edit_task

app_name='task'
urlpatterns = [
    path('',TaskClassView.as_view(),name='TaskClassView'),
    path('form/',new_task,name='new_task'),
    path('delete-task/<int:pk>/',delete_task,name='delete_task'),
    path('edit_task/<int:pk>/',edit_task,name='edit_task'),
]
