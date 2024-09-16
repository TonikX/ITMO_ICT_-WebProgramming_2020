from django.forms import ModelForm
from board.models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['tag','text']