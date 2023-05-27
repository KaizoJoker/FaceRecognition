from django import forms
from .models import Profile
from .models import Lecturer

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'shift':TimeInput()
        }
        exclude = ['present','updated']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['matricNo'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        #self.fields['image'].widget.attrs['class'] = 'form-control'


class Lecturer(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Lecturer, self).__init__(*args, **kwargs)
        self.fields['className'].widget.attrs['class'] = 'form-control'
        self.fields['lecturerName'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'
