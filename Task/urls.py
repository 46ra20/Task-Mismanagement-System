from django.urls import path
from .views import AddTask,getTask,editTask,deleteTask
urlpatterns = [
    path('addtask/',AddTask,name='addtask'),
    path('showtask/',getTask,name='showtask'),
    path('edittask/<int:id>',editTask,name='edittask'),
    path('deletetask/<int:id>',deleteTask,name='deletetask'),
]