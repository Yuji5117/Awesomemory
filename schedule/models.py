from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Schedule(models.Model):
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE) 
    date        = models.DateField('Date')
    title       = models.CharField('Title', max_length=50)
    content     = models.CharField('content', max_length=80, blank=True)
    created_at  = models.DateTimeField('Created date', default=timezone.now)

    def __str__(self):
        return self.summary
