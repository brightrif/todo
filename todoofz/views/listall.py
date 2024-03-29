from django.views import generic
from todoofz.models import Task

class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = 'listall.html'
    context_object_name = 'task_list'
