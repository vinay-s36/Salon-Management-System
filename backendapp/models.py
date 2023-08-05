from django.db import models


class user_details(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    emailid = models.EmailField()


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('fixed', 'Fixed'),
        ('pending', 'Pending'),
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.service} - {self.date} {self.time} - {self.status}"


class Appointment(models.Model):
    appointment_number = models.IntegerField()
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    # Add any other fields as needed

    def __str__(self):
        return self.name


class admin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
