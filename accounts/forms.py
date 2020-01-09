from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model

# To use users.CustomUser #
User = get_user_model()


class SignupForm(UserCreationForm):

    # add extra fileds for signup if you want

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)