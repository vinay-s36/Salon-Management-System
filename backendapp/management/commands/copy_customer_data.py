from django.core.management.base import BaseCommand
from backendapp.models import customers, user_appointments, user_details


class Command(BaseCommand):
    help = 'Copy data from user_appointments and user_details to Customer table'

    def handle(self, *args, **kwargs):
        # Get data from user_appointments and user_details tables
        appointments = user_appointments.objects.all()
        users = user_details.objects.all()

        # Iterate through the records and create corresponding Customer objects
        for appointment in appointments:
            try:
                user = users.get(username=appointment.name)
                customer = customers.objects.create(
                    name=appointment.name,
                    phone_number=appointment.phone,
                    email=user.emailid,
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Created Customer object: {customer}'))
            except user_details.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f'User details not found for {appointment.name}'))

        self.stdout.write(self.style.SUCCESS('Data copy completed.'))
