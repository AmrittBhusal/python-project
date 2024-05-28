from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=120)
    Email=forms.EmailField(max_length=120)