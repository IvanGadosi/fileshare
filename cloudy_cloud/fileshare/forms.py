from django import forms
from .models import SharedFile


class UploadForm(forms.ModelForm):
    class Meta:
        model=SharedFile
        fields=(
            'file',
            'file_key',
        )
        widgets = {'file_key': forms.HiddenInput()}