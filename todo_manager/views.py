from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

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


class TaskCompletionView(generic.View):
    model = Task

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(self.model, id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(
            reverse_lazy("todo_manager:task-list")
        )
