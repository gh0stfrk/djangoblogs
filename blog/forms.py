from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your blog title'}),
      'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your blog content here'}),
    }
        
    
