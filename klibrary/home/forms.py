from django import forms
from .models import Books

class Book_list(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

        labels = {
            'name': 'Book Name',
            'desc': 'Description',
            'price': 'Price (Rs.)',
            'email': 'Email Address',
            'image': 'Book Cover Image',
        }

        widgets ={

           'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'desc' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'about the book'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your email'}),
            'price' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter your price'}),
            'image' : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }