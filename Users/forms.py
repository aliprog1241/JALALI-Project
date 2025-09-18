from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_national_code(self):
        code = self.cleaned_data.get('national_code')
        if len(code) != 10:
            raise forms.ValidationError("کد ملی باید دقیقا ۱۰ رقم باشد.")
        return code

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        parts = full_name.split(" ")
        if len(parts) != 2:
            raise forms.ValidationError("نام کامل باید شامل نام و نام خانوادگی باشد.")
        first_name, last_name = parts
        if not (first_name[0].isupper() and first_name[1:].islower()):
            raise forms.ValidationError("نام باید با حرف بزرگ شروع شود و بقیه کوچک باشند.")
        if not (last_name[0].isupper() and last_name[1:].islower()):
            raise forms.ValidationError("نام خانوادگی باید با حرف بزرگ شروع شود و بقیه کوچک باشند.")
        return full_name
