from django import forms
from zimarinapp.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = [
            "text",
            "type",
            "importance",
        ]
