from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=(
            'email',
            'question',
            'question_detail',
        )
        widgets = {'question_detail': forms.Textarea(attrs={'rows':3,})}