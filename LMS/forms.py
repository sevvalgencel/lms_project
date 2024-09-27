# LMS/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Adınız Soyadınız',
        max_length=100,

    )
    email = forms.EmailField(
        label='Email adresiniz',

    )
    message = forms.CharField(
        label='',
        label_suffix='',
        widget=forms.Textarea(attrs={'placeholder': 'Mesajınızı buraya yazın...'}),
    )


