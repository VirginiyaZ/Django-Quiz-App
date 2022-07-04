from dataclasses import fields
from django import forms
from question.models import Question, Answer

from ckeditor.widgets import CKEditorWidget


class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}), required=True)
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = ('title', 'body')


class AnswerForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Answer
        fields = ('body',)

