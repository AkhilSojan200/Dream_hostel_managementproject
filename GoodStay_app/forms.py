from django import forms
from django.forms import TimeInput

from GoodStay_app.models import Custom_student, Custom_warden, Login, RoomDetails, Complaints, Schedule, Notification, \
    Fee_payment
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
        fields = 'name','address','phone_no'


class WardenForm(forms.ModelForm):
    class Meta:
        model = Custom_warden
        fields = 'name','address','phone_no','occupation'

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

class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = Fee_payment
        fields = [ 'date', 'amount', 'payment_mode', 'credit_card_cvv', 'bank_account_number', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'credit_card_cvv': forms.TextInput(attrs={'maxlength': '4'}),
            'bank_account_number': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 5, 'maxlength': '500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Conditionally include fields based on payment mode
        payment_mode = self.data.get('payment_mode') or self.instance.payment_mode
        if payment_mode == 'credit_card':
            self.fields['credit_card_cvv'].required = True
            self.fields['bank_account_number'].required = False
        else:
            self.fields['credit_card_cvv'].required = False

        if payment_mode == 'bank_transfer':
            self.fields['bank_account_number'].required = True
        else:
            self.fields['bank_account_number'].required = False
