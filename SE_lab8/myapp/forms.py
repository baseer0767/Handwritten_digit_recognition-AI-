from django import forms

class ConditionForm(forms.Form):
    a = forms.IntegerField(label="A")
    b = forms.IntegerField(label="B")
    c = forms.IntegerField(label="C")
    d = forms.IntegerField(label="D")
