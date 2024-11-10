from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['name', 'userid', 'email', 'group', 'role', 'employment_type', 'company_name', 'ip_clearance_level', 'catalog_task_id']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        userid = cleaned_data.get("userid")

        # Trim spaces
        if name:
            cleaned_data["name"] = name.strip()
        if userid:
            cleaned_data["userid"] = userid.strip()
        
        # Handle other custom validations if required

        return cleaned_data
