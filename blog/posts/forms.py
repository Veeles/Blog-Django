from django import forms
from .models import Comment
class Comments_form(forms.ModelForm):    

    class Meta:
        model = Comment
        fields = [ 'contents']
        widgets = {
            'contents':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write your comment here...'})
        }