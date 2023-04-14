from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요',
            }
        ),
    )
    movie = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영화를 입력하세요',
            }
        ),
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': '포스터',
            }
        ),
    )
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'comment',
                'class': 'form-control',
                'placeholder': '댓글을 입력하세요',
                'aria-label': "Recipient's username",
                'aria-describedby': 'button-addon2',
            }
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)