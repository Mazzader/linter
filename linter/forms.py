from django import forms

from linter.models import Document


class JsFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile',)
