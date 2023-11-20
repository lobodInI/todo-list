from django import forms

from todo_manager.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        label="deadline",
        required=False,
        widget=forms.DateTimeInput(
            format="%Y-%m-%d %H:%M",
            attrs={"type": "datetime-local"}
        ),
        input_formats=["%Y-%m-%d %H:%M"]
    )

    class Meta:
        model = Task
        fields = "__all__"
