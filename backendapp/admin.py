from django.contrib import admin
from .models import user_appointments, customers

admin.site.register(user_appointments)
admin.site.register(customers)
