from django.db import models
from datetime import datetime


class Message(models.Model):
    email=models.EmailField(max_length=100)
    question=models.CharField(max_length=100)
    date_sent=models.DateTimeField(default=datetime.now, editable=False)
    question_detail=models.TextField()

    class Meta:
        verbose_name_plural = "messages"

    def __str__(self):
        return "{}_{}".format(self.question_category, self.date_sent)
