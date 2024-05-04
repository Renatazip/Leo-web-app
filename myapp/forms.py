from django import forms
from .models import DiaryNote

class DiaryNoteForm(forms.ModelForm):
    class Meta:
        model = DiaryNote
        fields = ['text_description', 'photo', 'time', 'level_before', 'reason_of_eat', 'level_after', 'feelings_after_eating', 'comment']
        labels = {
            'text_description': 'Text Description',
            'photo': 'Photo',
            'level_before': 'Level Before Eating',
            'reason_of_eat': 'Reason of Eating',
            'level_after': 'Level After Eating',
            'feelings_after_eating': 'Feelings After Eating',
            'comment': 'Comment',
        }
        widgets = {
            'text_description': forms.TextInput(attrs={'placeholder': 'Enter text description'}),
            'photo': forms.ClearableFileInput(attrs={'placeholder': 'Choose a photo'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment here'}),
        }
