from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import AboutPage

class AboutPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = AboutPage
        fields = '__all__'
