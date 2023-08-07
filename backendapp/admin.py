from django.contrib import admin
from .models import user_appointments, user_details, customers

admin.site.register(user_appointments)
admin.site.register(user_details)
admin.site.register(customers)
