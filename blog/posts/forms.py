from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
class CommentsForm(forms.ModelForm):    

    class Meta:
        model = Comment
        fields = [ 'contents']
        widgets = {
            'contents':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write your comment here...'})
        }



class NewPost(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'description', 'photo', 'author']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write title'}),
            'photo':forms.ClearableFileInput(attrs={'class':'btn btn-danger'}),
        }

        author = forms.ModelChoiceField(queryset=User.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select author'})
    )
        

class UpdatePost(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'description', 'photo']
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'photo':forms.ClearableFileInput(attrs={'class':'btn btn-danger'}),
            }