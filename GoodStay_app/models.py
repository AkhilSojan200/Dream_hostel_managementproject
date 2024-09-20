
from django.contrib.auth.models import AbstractUser, Login
# from django.utils.html import escape, make_safe
from django.core.exceptions import ValidationError



from django.db import models
from django.utils import timezone


# Create your models here.

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_warden = models.BooleanField(default=False)



class Custom_student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    phone_no = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"


class Custom_warden(models.Model):
    user1 = models.OneToOneField(Login, on_delete=models.CASCADE)
    name=models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    phone_no = models.IntegerField(null=True,blank=True)
    occupation = models.CharField(max_length=250,blank=True,null=True)


class RoomDetails(models.Model):

    Room_no = models.CharField(max_length=250, blank=True, null=True)
    details = models.CharField(max_length=250,blank=True,null=True)
    Block_name = models.CharField(max_length=250, blank=True, null=True)
    No_of_beds = models.CharField(max_length=250, blank=True, null=True)
    Monthly_fee = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.Room_no} - {self.Block_name}"


class Complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=250, blank=True, null=True)
    complaint = models.TextField(max_length=250, blank=True, null=True)
    date = models.DateField( blank=True, null=True)
    reply = models.TextField(max_length=250, blank=True, null=True)


class Schedule(models.Model):
    user = models.ForeignKey(Custom_student, on_delete=models.DO_NOTHING)
    hostel = models.ForeignKey(RoomDetails, on_delete=models.DO_NOTHING)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)



class Booking(models.Model):
    user = models.ForeignKey(Custom_student, on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(RoomDetails, on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)


class Notification(models.Model):
    date = models.DateField(blank=True, null=True)
    notice_heading = models.CharField(max_length=250,blank=True,null=True)
    notice_details = models.TextField(max_length=250,blank=True,null=True)


class MonthlyPayment:
    pass


from django.db import models
from django.core.exceptions import ValidationError


class Fee_payment(models.Model):
    user = models.ForeignKey(Custom_student, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    PAYMENT_MODES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODES)

    # Credit Card details (Only used when payment_mode is 'credit_card')
    credit_card_cvv = models.CharField(max_length=4, blank=True, null=True)

    # Bank Transfer details (Only used when payment_mode is 'bank_transfer')
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)

    description = models.TextField(max_length=250, blank=True, null=True)

    def clean(self):
        """
        Custom validation logic to ensure CVV is provided for credit card payments
        and account number is provided for bank transfers.
        """
        if self.payment_mode == 'credit_card' and not self.credit_card_cvv:
            raise ValidationError("CVV is required for credit card payments.")

        if self.payment_mode == 'bank_transfer' and not self.bank_account_number:
            raise ValidationError("Bank account number is required for bank transfers.")

    def save(self, *args, **kwargs):
        # Call the clean method to ensure the custom validations are checked
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment by {self.user} on {self.date}"
