from django import forms
from .models import Video

class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'upload')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }