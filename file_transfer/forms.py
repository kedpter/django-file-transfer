from django import forms
from file_transfer.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('document', )

