# LMS/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

from django import forms
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**********'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Bu email ile kayıtlı bir kullanıcı bulunamadı.")

        if not user.check_password(password):
            raise forms.ValidationError("Hatalı şifre.")
        
        self.user = authenticate(username=user.username, password=password)
        if not self.user:
            raise forms.ValidationError("Giriş yapılamadı, lütfen bilgilerinizi kontrol edin.")
        
        return self.cleaned_data

    def get_user(self):
        return self.user

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


