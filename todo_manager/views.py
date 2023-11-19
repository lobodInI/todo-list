from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_manager.forms import TaskCreateForm
from todo_manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_manager:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_manager:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_manager:tag-list")


def completing_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("todo_manager:task-list")
    )
