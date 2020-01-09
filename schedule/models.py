from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    date = models.DateField('Date')
    summary = models.CharField('Title', max_length=50)
    description = models.TextField('Text', blank=True)
    created_at = models.DateTimeField('Created date', default=timezone.now)

    def __str__(self):
        return self.summary
