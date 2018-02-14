from django import forms
from .models import Property

class property_form(forms.Form):
        property_name = forms.CharField()
        property_address_line_1 = forms.CharField()
        property_address_line_2 = forms.CharField()
        property_address_line_3 = forms.CharField()
        property_address_line_4 = forms.CharField()
        unit_name = forms.CharField()
        tenant_name = forms.CharField()
        lease_start_date = forms.DateField()
        lease_end_date = forms.DateField()
        lease_years = forms.IntegerField()
        current_rent = forms.DecimalField()
