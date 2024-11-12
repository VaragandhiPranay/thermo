from django import forms
from .models import UserData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'name', 'user_id', 'email', 'group', 'role', 'employment_type',
            'company_name', 'ip_clearance_level', 'catalog_tasks_id'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'user_id': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
            'group': forms.Select(attrs={'autocomplete': 'off'}),
            'role': forms.Select(attrs={'autocomplete': 'off'}),
            'employment_type': forms.Select(attrs={'autocomplete': 'off'}),
            'company_name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'ip_clearance_level': forms.Select(attrs={'autocomplete': 'off'}),
            'catalog_tasks_id': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()
        # Remove trailing whitespace from inputs
        for field, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[field] = value.strip()
        return cleaned_data
