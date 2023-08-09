from django.db import models


class user_details(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    emailid = models.EmailField()


class user_appointments(models.Model):
    appointment_number = models.IntegerField(primary_key=True)
    service = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name}'s Appointment for {self.service} on {self.date} at {self.time}"


class admin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class customers(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
