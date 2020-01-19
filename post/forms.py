from django import forms

from .models import Post, Category, Comment, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'text'] 
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['multi_images',]


ImageModelFormSet = forms.modelformset_factory(Image, form=ImageForm, fields=('multi_images', ), extra=5, max_num=5)

# class PostSearchForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['category', 'title']
# 
# class PostSearchForm(forms.Form):
#     category = forms.ModelChoiceField(
#         queryset=Post.objects.all(),
#         required=False 
#     )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]




