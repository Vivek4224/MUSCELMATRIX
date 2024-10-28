from django.contrib import admin
from .models import Clients, ClientProfile, ClientAddress, ClientMeasurements

class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'email', 'mobile']
    search_fields = ['client_id', 'email','mobile']

admin.site.register(Clients, ClientAdmin)

class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'first_name', 'last_name', 'gender', 'dob']
    list_filter = ['gender']

admin.site.register(ClientProfile, ClientProfileAdmin)

admin.site.register(ClientAddress)

admin.site.register(ClientMeasurements)

