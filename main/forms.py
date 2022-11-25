from django import forms
from .models import Academic_year
class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic_year
        fields = '__all__'

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the year, eg:2017-2018'})
        }