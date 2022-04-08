from django.db import models
from django.http import request

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    clinic_name = models.TextField(blank=False)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]

class clinic(models.Model):
    clinic_name=models.CharField(max_length=25)
    doctor_name=models.CharField(max_length=25)
    qualification=models.CharField(max_length=50)
    # hospital_name=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.clinic_name 