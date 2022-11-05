from django import forms
from django.core.exceptions import ValidationError
from .models import VacationRequest


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class VacationRequestForm(forms.ModelForm):
    class Meta:
        model = VacationRequest
        fields = ['start_date', 'finish_date', 'reason']
        widgets = {
            'start_date': DatePickerInput(),
            'finish_date': DatePickerInput(),
        }

    def clean_dates(self):
        start_date = self.cleaned_data['start_date']
        finish_date = self.cleaned_data['finish_date']
        if finish_date <= start_date:
            raise ValidationError(
                "Start date cannot be bigger than finish date")
        return start_date, finish_date

    def save(self, user, account, commit=True):
        vacation_request = VacationRequest.objects.create(
            user=user,
            start_date=self.cleaned_data['start_date'],
            finish_date=self.cleaned_data['finish_date'],
            reason=self.cleaned_data['reason'],
            account=account,
        )
        return vacation_request
