from django import forms
from .models import Comment
from allauth.account.forms import SignupForm

class CommentForm(forms.ModelForm):
class Meta:
model = Comment
fields = ('body',)

class CustomSignupForm(SignupForm):
def **init**(self, *args, **kwargs):
super().**init**(*args, **kwargs)

```
    if 'password1' in self.fields:
        self.fields['password1'].help_text = ""
        self.fields['password1'].widget.attrs.pop('aria-describedby', None)

    if 'password2' in self.fields:
        self.fields['password2'].help_text = ""
        self.fields['password2'].widget.attrs.pop('aria-describedby', None)
```
