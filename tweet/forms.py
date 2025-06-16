from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import tweet


class tweetForm(forms.ModelForm):
    class Meta:
        model  = tweet
        fields = ['text','photo','dis',]
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Manually saving email
        if commit:
            user.save()
        return user
