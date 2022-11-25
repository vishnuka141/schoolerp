from django import forms
from .models import PaymentType,Payment

class PaymentTypeForm(forms.ModelForm):
    fee_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fee type eg: Term 1'}))
    class Meta:
        model = PaymentType
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
