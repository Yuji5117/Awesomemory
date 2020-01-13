from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, User



class SignupForm(UserCreationForm):

    # add extra fileds for signup if you want

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "gender", 'age')

    # To add class in the form #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # To add 'class="form-control"' into everyfield of Profile molde  #
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'