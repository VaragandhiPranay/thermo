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
            'group': forms.Select(),
            'role': forms.Select(),
            'employment_type': forms.Select(),
            'ip_clearance_level': forms.Select()
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
