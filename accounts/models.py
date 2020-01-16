from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# To use users.CustomUser #
User = get_user_model()


class UserProfile(models.Model):

    GENDER_CHOICE = (
        ('Male', "Male"),
        ('Female', "Female"),
    )

    first_name    = models.CharField("First Name", max_length=50, blank=True)
    last_name     = models.CharField("Last Name", max_length=50, blank=True)
    profile_image = models.ImageField("Profile Image", default='default.jpg', upload_to='profile/%y/%m/%d', null=True, blank=True)
    gender        = models.CharField("Gender", max_length=6, choices=GENDER_CHOICE, blank=True)
    age           = models.IntegerField("Age", blank=True, null=True)
    user          = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} Profile'

