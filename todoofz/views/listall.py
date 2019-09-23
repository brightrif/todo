from django.views import generic
from todoofz.models import TodoList

class TaskListView(generic.ListView):
    model = TodoList
    queryset = TodoList.objects.all()
    template_name = 'listall.html'
    context_object_name = 'task_list'
