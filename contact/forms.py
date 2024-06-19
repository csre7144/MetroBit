from django import forms
from .models import ContactList

class ContactListForm(forms.ModelForm):
      class Meta:
            model = ContactList
            fields = '__all__'