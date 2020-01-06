from django import forms
from .models import Review
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')

