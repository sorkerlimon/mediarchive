from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    BLOOD_TYPE = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER_TYPE, default="male")
    blood = models.CharField(max_length=255, blank=True, null=True, choices=BLOOD_TYPE, default="AB+")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    dob = models.DateField(max_length=8,blank=True,null=True)
    phone_number = PhoneNumberField(blank=True,null=True)

    def __str__(self):
        return str(self.username)
