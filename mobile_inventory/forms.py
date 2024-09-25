from .models import Phone
from django.forms import forms


class PhoneForm(forms.Form):
    class Meta:
        model = Phone
        fields = '__all__'
