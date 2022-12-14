from django import forms

class availibleFrom(forms.Form):
    room_type = (
        ('SBD', 'SINGLE_BED'), # what kind of room it is
        ('DBD', 'DOUBLE_BED'),
        ('VIP', 'DELUXE_ROOM'),
    
    )
    room_type = forms.ChoiceField(choices=room_type, required=True)
    checking_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    checking_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
