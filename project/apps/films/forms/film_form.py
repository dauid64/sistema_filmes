from django import forms
from ..models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'description', 'assisted_in', 'would_like']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'assisted_in': 'Assistido em',
            'would_like': 'Gostaria de assistir'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'assisted_in': forms.TextInput(
                attrs={
                    'class': 'form-control mask-date'
                }
            ),
            'would_like': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )
        }
