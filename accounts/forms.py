from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, label="Phone Number")

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'email')

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("Phone number already exists.")
        return phone


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=15,
        label="Phone Number",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.", code='inactive')
