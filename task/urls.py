from django.urls import path

from task.views import TaskClassView,delete_task,edit_task,toggle

app_name='task'
urlpatterns = [
    path('',TaskClassView,name='TaskClassView'),
    # path('form/',new_task,name='new_task'),
    path('delete-task/<int:pk>/',delete_task,name='delete_task'),
    path('edit-task/<int:pk>/',edit_task,name='edit_task'),
    path('toggle/<int:pk>/',toggle,name="toggle"),
]
