from django.db import models

# Create your models here.

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.name

