"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'maxlength': '120'}),
            'quantity': forms.NumberInput()
        }
    
    name = forms.CharField(min_length=1, max_length=35) 
    quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)]) 
