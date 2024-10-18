from django.db import models
from django.contrib.auth.hashers import make_password

from MMApps.master.models import TimeStamp
from MMApps.master.helpers.create_primary_key import generate_primary_key

class Clients(TimeStamp):
    POST_FIX = 'client'
    client_id = models.CharField(primary_key=True, max_length=255,null=False,blank=True)
    email = models.EmailField(max_length=255,null=False,blank=False,unique=True)
    mobile = models.CharField(max_length=50,null=False,blank=False,unique=True)
    password = models.CharField(max_length=255,null=False,blank=False)
    is_verified_tac = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.client_id:
            self.client_id = generate_primary_key(self.POST_FIX)
            self.password = make_password(self.password)
        super(Clients, self).save(*args, **kwargs)