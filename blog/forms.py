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
    # Force override widgets to remove aria-describedby AFTER allauth processing
    if 'password1' in self.fields:
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'autocomplete': 'new-password',
            }
        )

    if 'password2' in self.fields:
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'autocomplete': 'new-password',
            }
        )
```
