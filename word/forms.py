from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="emailアドレスは必須です")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']