from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# imagelit #
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


# To use users.CustomUser #
User = get_user_model()



class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    # user       = models.OneToOneField(User, on_delete=models.CASCADE)
    title      = models.CharField('タイトル', max_length=50)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail  = ImageSpecField(source='image', processors=[ResizeToFill(250,250)])
    image      = models.FileField('画像', upload_to='photos/%y/%m/%d', null=True, blank=True)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={'pk' : self.pk})


class Comment(models.Model):
    text = models.TextField('Comment')
    post = models.ForeignKey(Post, verbose_name='対象メモリー', on_delete=models.CASCADE)

    """ Commentに結びつく """
    parent = models.ForeignKey('self', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]



