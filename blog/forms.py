from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

# CHOICE = (('Anonymous', 'Anonymous'), (User.objects.all().filter(), User.objects.all()))
class CommentForm(forms.ModelForm):
    # name = forms.ChoiceField(choices = CHOICE)
    class Meta:
        model = Comment
        # fields = ['name','body']
        exclude = ["name"]

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }