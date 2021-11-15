
from django import forms
from .models import Agency


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ('name_agency', 'comments')

'''
class LdProjForm(forms.ModelForm):
    class Meta:
        model = LdProj
        fields = ('proj_name','subject_name','doc_name_pattern','doc_name','doc_number','page_type','format_doc')

'''