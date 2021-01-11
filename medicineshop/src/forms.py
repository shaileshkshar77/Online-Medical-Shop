
from django import forms

class prescription(forms.Form):
    c_id=forms.CharField()
    img=forms.ImageField()

    def __str__(self):
        return self.m_id
