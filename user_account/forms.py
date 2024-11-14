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
            'employment_type': forms.TextInput(attrs={'autocomplete': 'off', 'list': 'employment_type_list'}),
            'ip_clearance_level': forms.Select(attrs={'autocomplete': 'off'}),
            'catalog_tasks_id': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super().clean()
        employment_type = cleaned_data.get('employment_type')

        # Ensure `employment_type` is provided and valid
        if not employment_type:
            self.add_error('employment_type', 'Please provide an employment type.')

        return cleaned_data
