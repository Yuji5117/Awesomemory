from django import forms

from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'text']
    
PostModelFormSet = forms.modelformset_factory(
    Post, form=PostForm,
    extra=3
)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]




