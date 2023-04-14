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
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': '포스터',
            }
        ),
    )

    rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'min': 1,
                'max': 100,
                'value': 100,
                'class': 'form-control',
                'placeholder': '점수를 입력해주세요.',
            },
        ),
    )   

    CHOICES = (('액션' , '액션'), ('SF', 'SF'), ('로맨스', '로맨스'), ('드라마', '드라마'), ('스릴러', '스릴러'))
    genre = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image', 'rating', 'genre',)


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