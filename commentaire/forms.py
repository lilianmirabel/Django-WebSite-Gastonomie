from restaurant.models import Restaurant, TypeResto, Commentaire
from django.forms import ModelChoiceField
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from restaurant.models import TypeResto

class ajouterCommentaireForm(forms.ModelForm):
    
    class Meta:
        model = Commentaire
        fields = ['commentaire', 'note']
        labels = {'commentaire': 'Commentaire', 'note': 'Note'}
        help_texts = {'commentaire': 'Écrivez votre commentaire ici', 'note': 'Donnez une note au restaurant (0-5)'}
        error_messages = {'commentaire': {'required': 'Ce champ est obligatoire'}, 'note': {'required': 'Ce champ est obligatoire'}}
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Ajouter un commentaire',
                'commentaire',
                'note',
            ),
            ButtonHolder(
                Submit('submit', 'Ajouter', css_class='btn btn-primary')
            )
        )

    def clean_note(self):
        note = self.cleaned_data['note']
        if note < 0 or note > 5:
            raise forms.ValidationError("La note doit être comprise entre 0 et 5.")
        return note

class modifierCommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['commentaire', 'note']
        labels = {'commentaire': 'Commentaire', 'note': 'Note'}
        help_texts = {'commentaire': 'Écrivez votre commentaire ici', 'note': 'Donnez une note au restaurant (0-5)'}
        error_messages = {'commentaire': {'required': 'Ce champ est obligatoire'}, 'note': {'required': 'Ce champ est obligatoire'}}
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Ajouter un commentaire',
                'commentaire',
                'note',
            ),
            ButtonHolder(
                Submit('submit', 'Modifier', css_class='btn btn-primary')
            )
        )     

    def clean_note(self):
        note = self.cleaned_data['note']
        if note < 0 or note > 5:
            raise forms.ValidationError("La note doit être comprise entre 0 et 5.")
        return note   