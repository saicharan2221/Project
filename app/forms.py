from django import forms
from app.models import *


class LeaveApplicationform(forms.ModelForm):
    class Meta:
        model=LeaveApplication
        fields=['date_of_application','start_date','end_date','leave_description','user'] 
        date_of_application=models.DateField(default=now())
        start_date=models.DateField()
        end_date=models.DateField()
        leave_description=models.CharField
        # user=autofill