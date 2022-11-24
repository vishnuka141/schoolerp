from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    # parent_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Student
        fields = '__all__'

        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'parent_name':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'admission_number':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_certificate':forms.FileInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
            'batch':forms.Select(attrs={'class':'form-select'})

        }
                    

