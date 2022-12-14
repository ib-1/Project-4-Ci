from django import forms

class availibleFrom(forms.Form):
    checking_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    checking_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
