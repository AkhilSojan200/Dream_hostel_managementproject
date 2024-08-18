from django import forms
from django.forms import TimeInput

from GoodStay_app.models import Custom_student, Custom_warden, Login, RoomDetails, Complaints, Schedule, Notification
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    username = forms.CharField(max_length=250)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('username','password1','password2')

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Custom_student
        fields = '__all__'


class WardenForm(forms.ModelForm):
    class Meta:
        model = Custom_warden
        fields = '__all__'

#
class RoomDetailsForm(forms.ModelForm):
    class Meta:
        model = RoomDetails
        fields = '__all__'



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class ComplaintsForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model =  Complaints
        fields = ('date','subject','complaint')




class ScheduleForm(forms.ModelForm):
    date_in = forms.DateField(widget=DateInput)
    date_out = forms.DateField(widget=DateInput)

    class Meta:
        model = Schedule
        fields = ('hostel','date_in','date_out')



class NoticeForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = '__all__'
