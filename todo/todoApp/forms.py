from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    # to add placeholder in the input form
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
        # pass all the fields to the form
		fields = '__all__' 
		# fields = ['title']