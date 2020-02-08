from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# To use users.CustomUser #
User = get_user_model()

class Post(models.Model):
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    title      = models.CharField('タイトル', max_length=50)
    category   = models.CharField('カテゴリー', max_length=50, null=True, blank=True)
    image      = models.FileField('画像', upload_to='photos/%y/%m/%d', null=True, blank=True)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={'pk' : self.pk})

class Image(models.Model):
    post         = models.ForeignKey(Post, related_name='multi_img', on_delete=models.CASCADE)
    multi_images = models.FileField('画像', upload_to='multi_photos', null=True, blank=True)
    uploaded_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + 'Image'





