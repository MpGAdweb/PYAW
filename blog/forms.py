from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Comentário')
