from django import forms
from .models import Comment
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'password1' in self.fields:
            self.fields['password1'].help_text = ""
            self.fields['password1'].widget.attrs.pop('aria-describedby', None)

        if 'password2' in self.fields:
            self.fields['password2'].help_text = ""
            self.fields['password2'].widget.attrs.pop('aria-describedby', None)