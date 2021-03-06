from django import forms

from .models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'text'] 
        widgets = {
            'text': forms.Textarea(attrs={'rows':6, 'cols':15}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].widget = post.TextField(Textarea(attrs={'cols': '80', 'rows': '3'}))  

        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['multi_images',]

# formset for multi-forms #
ImageModelFormSet = forms.modelformset_factory(Image, form=ImageForm, fields=('multi_images', ), extra=5, max_num=5)





