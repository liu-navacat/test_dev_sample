from django import forms
from .models import Project

# class projectForm(forms.Form):
#     name = forms.CharField(label='名称',max_length=100)
#     describe = forms.CharField(label='描述',widget=forms.Textarea)

class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','describe']