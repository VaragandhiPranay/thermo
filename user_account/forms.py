from django import forms
from .models import UserData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'name', 'user_id', 'email', 'group', 'role', 'employment_type',
            'ip_clearance_level', 'catalog_tasks_id'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'user_id': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
            'group': forms.Select(attrs={'autocomplete': 'off'}),
            'role': forms.Select(attrs={'autocomplete': 'off'}),
            'employment_type': forms.Select(choices=[('MSD', 'MSD'), ('other', 'Other')], 
                                             attrs={'id': 'id_employment_type'}),
            'ip_clearance_level': forms.Select(attrs={'autocomplete': 'off'}),
            'catalog_tasks_id': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the "Company Name" field, initially hidden
        self.fields['company_name'] = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Enter Company Name if "Other"'}),
            label="Company Name (if Other)"
        )
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()
        employment_type = cleaned_data.get('employment_type')
        company_name = cleaned_data.get('company_name')

        # If "Other" is selected for employment type, company name must be provided
        if employment_type == 'other' and not company_name:
            self.add_error('company_name', 'Please provide a company name when selecting "Other".')
        elif employment_type == 'other' and company_name:
            cleaned_data['employment_type'] = company_name  # Store company name in employment_type field

        return cleaned_data
