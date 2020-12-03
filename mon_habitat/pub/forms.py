from django.db.models.base import Model
from django.forms import Textarea, TextInput, NumberInput, Select, FileInput
from .models import Publication




class PublicationForm(forms.ModelForm):
    class Meta:
    model = Publication
    fields = ["first_name",
        "last_name",
        "agency_name",
        "city",
        "categories",
        "status",
        "phone_number_1",
        "phone_number_2",
        "description",
        "image_one"
    ]
    widgets = {
        'first_name': TextInput(attrs={'class': 'form-control'}),
        'last_name': TextInput(attrs={'class': 'form-control'}),
        'agency_name': TextInput(attrs={'class': 'form-control'}),
        'city': Select(attrs={'class': 'form-control', 'placeholder':'Choisir une ville'} ),
        'categories': Select(attrs={'class': 'form-control', 'placeholder':'Choisir une catégorie'}),
        'status': Select(attrs={'class': 'form-control', 'placeholder':'Choisir un statut'}),
        'phone_number_1': NumberInput(attrs={'class': 'form-control'}),
        'phone_number_2': NumberInput(attrs={'class': 'form-control'}),
        'description': Textarea(attrs={'class': 'form-control'}),
        'image_one': FileInput(attrs={'class': 'form-control'}),
    }