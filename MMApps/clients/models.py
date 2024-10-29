from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string

from MMApps.master.models import TimeStamp
from MMApps.master.helpers.create_primary_key import generate_primary_key

import os

class Clients(TimeStamp):
    POST_FIX = 'client'
    client_id = models.CharField(primary_key=True, max_length=255,null=False,blank=True)
    email = models.EmailField(max_length=255,null=False,blank=False,unique=True)
    mobile = models.CharField(max_length=50,null=False,blank=False,unique=True)
    password = models.CharField(max_length=255,null=False,blank=False)
    is_verified_tac = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    otp = models.CharField(max_length=255, default='123456')

    def save(self, *args, **kwargs):
        if not self.client_id:
            self.client_id = generate_primary_key(self.POST_FIX)
            self.password = make_password(self.password)
        super(Clients, self).save(*args, **kwargs)

class ClientProfile(TimeStamp):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    POST_FIX = 'client_profile'
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='clients')
    profile = models.ImageField(upload_to=f'{POST_FIX}s/', default='media/default-images/default_profile.png')
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the object is being updated or created for the first time
        is_new = self.pk is None
        try:
            existing_profile = ClientProfile.objects.get(pk=self.pk)
        except ClientProfile.DoesNotExist:
            existing_profile = None

        if self.profile and (is_new or (existing_profile and existing_profile.profile != self.profile)):
            if self.profile.name.startswith('default-images'):
                # Use the default image without changing the name
                new_filename = self.profile.name
                self.profile.name = os.path.join(new_filename)
            else:
                # Change the filename when a new image is uploaded
                base, ext = os.path.splitext(self.profile.name)
                new_filename = f"{self.client_id}_{self.POST_FIX}{ext}"
                self.profile.name = self.generate_unique_filename(new_filename)
                
        super(ClientProfile, self).save(*args, **kwargs)

    def generate_unique_filename(self, filename):
        # Generate a unique filename using the original filename and a random string
        base, ext = os.path.splitext(filename)
        unique_name = f"{base}_{get_random_string(length=8)}{ext}"  # e.g., 'client_profile_8h2k3d.jpg'
        return unique_name

class ClientAddress(TimeStamp):
    POST_FIX = 'client_address'
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='client_address')
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

class ClientMeasurements(TimeStamp):
    POST_FIX = 'client_measurements'
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='client_measurements')
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hip = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    body_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)