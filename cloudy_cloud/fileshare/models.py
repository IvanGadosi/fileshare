from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class OlderFilesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_created__lte=datetime.now()-timedelta(hours=24))


class SharedFile(models.Model):
    file_key=models.CharField(max_length=100, primary_key=True)
    date_created=models.DateTimeField(default=datetime.now, editable=False)
    file=models.FileField(upload_to="files/")
    paid=models.BooleanField(default=False)

    objects=models.Manager()
    older_files = OlderFilesManager()

    class Meta:
        verbose_name_plural = "sharedfiles"

    def __str__(self):
        return str(self.file.file).split('/')[-1]


@receiver(post_delete, sender=SharedFile)
def media_delete(sender, instance, **kwargs):
    instance.file.delete(False)