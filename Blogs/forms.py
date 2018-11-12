from django import forms


class BlogForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    post = forms.CharField(widget=forms.Textarea)