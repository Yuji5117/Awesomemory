from django import forms

from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'text'] 


# class CategoryForm(forms.ModelForm):



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]




