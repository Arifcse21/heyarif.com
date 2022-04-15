from django import forms

class PingForm(forms.Form):
    name    = forms.CharField(max_length=50, required=True)
    email   = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=250, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
