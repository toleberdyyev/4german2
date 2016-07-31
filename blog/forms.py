from django import forms
from .models import Post, Comment
from django.core.files.images import get_image_dimensions
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(
    label='Your title',
    widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Create a Interesting title for post...'}
    )
    )
    text = forms.CharField(
    label='Your Post',
    widget=forms.Textarea(
    attrs={'class': 'form-control', 'placeholder': 'Write your post bellow , please write something Interesting to catch more likezz <3 ... '}
    )
    )
    image =forms.ImageField(
    required=False,
    widget=forms.FileInput(
    attrs={'style':"display:none"}
    )
    )
    class Meta:
        model = Post
        fields = ('title', 'text','image',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(
    label='Your Comment',
    widget=forms.Textarea(
    attrs={'class': 'form-control', 'placeholder': 'comment ... post or someone ... ','rows':'3','maxlength':'140'}
    )
    )
    captcha=NoReCaptchaField()
    class Meta:
        model = Comment
        fields = ('text','parent')
