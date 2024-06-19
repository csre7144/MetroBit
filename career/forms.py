from django import forms
from .models import career

class careerList(forms.ModelForm):
      class Meta:
            model = career
            fields = '__all__'

      def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["firstname"].widget.attrs.update({"class": "form-re", "placeholder":"First Name"})
            self.fields["lastname"].widget.attrs.update({"class": "form-re", "placeholder":"Last Name"})
            self.fields["email"].widget.attrs.update({"class": "form-re", "placeholder":"Email"})
            self.fields["phone"].widget.attrs.update({"class": "form-re", "placeholder":"Phone:- +919876543210 (10 digit)"})
            self.fields["position"].widget.attrs.update({"class": "nice-select form-control wide", "placeholder":"Select Position"})
            self.fields["experience"].widget.attrs.update({"class": "nice-select form-control wide"})
            self.fields["join"].widget.attrs.update({"class": "nice-select form-control wide"})
            self.fields["description"].widget.attrs.update({"class": "form-re", "placeholder":"Tell me about yourself"})
            self.fields["document"].widget.attrs.update({"class": "resume-file"})