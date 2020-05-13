from .models import tasks
from django.forms import ModelForm
class taskForm(ModelForm):

    class Meta:
        model = tasks
        fields = ()