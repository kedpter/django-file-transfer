from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
            # also remove all the files with same name
            samefiles = File.objects.filter(document=name)
            for s in samefiles:
                s.delete()
        return name

# Create your models here.

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(storage=OverwriteStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.name

