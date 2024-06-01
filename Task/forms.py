from django.forms import ModelForm
from .models import TaskModels

class TaskForms(ModelForm):
    class Meta:
        model = TaskModels
        fields='__all__'