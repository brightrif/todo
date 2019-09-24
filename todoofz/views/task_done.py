from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from todoofz.models import Task
# from todo.utils import toggle_task_completed

def task_completed(task_id: int) -> bool:
    """Toggle the `completed` bool on Task from True to False or vice versa."""
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return True

    except Task.DoesNotExist:
        log.info(f"Task {task_id} not found.")
        return False

def task_done(request, task_id: int) -> HttpResponse:
    """Toggle the completed status of a task from done to undone, or vice versa.
    Redirect to the list from which the task came.
    """

    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)

        # redir_url = reverse(
        #     "listall",
        #     kwargs={"task_id": task.task.id},
        # )

        task_completed(task_id)
        messages.success(request, "Task status changed for '{}'".format(task.title))

        return redirect("listall")
