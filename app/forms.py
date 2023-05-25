from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    date_field = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Todo
        fields = ["title", "date_field"]
