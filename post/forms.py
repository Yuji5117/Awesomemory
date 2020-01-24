from django import forms

from .models import Post, Category, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'text'] 

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].widget = post.TextField(Textarea(attrs={'cols': '80', 'rows': '3'}))  

        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['multi_images',]

# formset for multi-forms #
ImageModelFormSet = forms.modelformset_factory(Image, form=ImageForm, fields=('multi_images', ), extra=5, max_num=5)


# might use this later #
# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ['text', ]




