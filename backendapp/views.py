from django.shortcuts import render, redirect
from .models import user_details, admin, user_appointments
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum
from datetime import date, timedelta
import random


def landing(request):
    return render(request, 'landing-page.html')


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    customer_count = user_appointments.objects.values(
        'phone').annotate(count=Count('phone')).count()
    appointment_count = user_appointments.objects.count()
    total_sales = user_appointments.objects.aggregate(total=Sum('price'))[
        'total'] or 0

    today = date.today()
    todays_sales = user_appointments.objects.filter(
        date=today).aggregate(total=Sum('price'))['total'] or 0

    yesterday = date.today() - timedelta(days=1)
    yesterdays_sales = user_appointments.objects.filter(
        date=yesterday).aggregate(total=Sum('price'))['total'] or 0

    start_date = today - timedelta(days=6)
    last_seven_days_sales = 0
    for day in range(7):
        sales_date = start_date + timedelta(days=day)
        daily_sales = user_appointments.objects.filter(
            date=sales_date).aggregate(total=Sum('price'))['total'] or 0
        last_seven_days_sales += daily_sales

    context = {
        'customer_count': customer_count,
        'appointment_count': appointment_count,
        'total_sales': total_sales,
        'todays_sales': todays_sales,
        'yesterdays_sales': yesterdays_sales,
        'last_seven_days_sales': last_seven_days_sales
    }
    return render(request, 'admin_dashboard.html', context)


def new(request):
    return render(request, 'admin_dashboard/new_appointments.html')


def accepted(request):
    return render(request, 'admin_dashboard/accepted_appointments.html')


def rejected(request):
    return render(request, 'admin_dashboard/rejected_appointments.html')


def invoice(request):
    return render(request, 'admin_dashboard/invoices.html')


def search_invoice(request):
    return render(request, 'admin_dashboard/search_invoice.html')


def contacts(request):
    return render(request, 'contacts.html')


def admin_login(request):
    return render(request, 'login-admin.html')


def spcl_service(request):
    return render(request, 'special_service.html')


def logincon(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = user_details.objects.get(emailid=username)
            if user.password == password:
                return redirect('/home')
            else:
                messages.error(
                    request, 'Incorrect username or password. Please try again.')
                return redirect('/login')
        except user_details.DoesNotExist:
            messages.error(request, 'User not found. Please check your email.')
            return redirect('/login')

    return render(request, 'login.html')


def signup(request):
    username = request.POST['username1']
    password = request.POST['password1']
    email = request.POST['email1']

    try:
        user = user_details(username=username,
                            password=password, emailid=email)
        user.save()
        return redirect('/login')
    except:
        return redirect('/login')


def adminsignin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = admin.objects.get(username=username)
            if user.password == password:
                return redirect('/admin-dashboard')
            else:
                messages.error(
                    request, 'Incorrect password. Please try again.')
                return redirect('/admin-login')
        except admin.DoesNotExist:
            messages.error(
                request, 'Username not found. Please check your username.')
            return redirect('/admin-login')

    return render(request, 'admin_login.html')


def generate_appointment_number():
    return random.randint(1000, 9999)


def appointment_details(request):
    if request.method == 'POST':
        service = request.POST.get('service', '')
        price = request.POST.get('price', '')
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')

        while True:
            appointment_number = generate_appointment_number()

            # Check if the generated appointment number already exists
            if not user_appointments.objects.filter(appointment_number=appointment_number).exists():
                break

        # Create and save the appointment object to the database
        appointment = user_appointments(
            service=service, name=name, phone=phone, date=date, time=time, appointment_number=appointment_number, price=price)
        appointment.save()

        # Return a response indicating successful form submission (you can customize this)
        return redirect('/services')


def display_all(request):
    appointments = user_appointments.objects.all().order_by('date', 'time')
    context = {
        'appointments': appointments
    }

    return render(request, 'admin_dashboard/all_appointments.html', context)


def appointments(request):
    user_appointment_data = user_appointments.objects.filter(
        name=request.user.username)
    return render(request, 'appointments.html', {'user_appointment_data': user_appointment_data})


def search_appointment(request):
    return render(request, 'admin_dashboard/search_appointment.html')


def search_appointment1(request):
    appointment = None
    no_records_found = False

    if request.method == 'POST':
        appointment_number = request.POST.get('appointment-number', '')
        try:
            appointment = user_appointments.objects.get(
                appointment_number=appointment_number)
        except user_appointments.DoesNotExist:
            no_records_found = True
    print(appointment)
    return render(request, 'admin_dashboard/search_appointment.html', {
        'appointment': appointment,
        'no_records_found': no_records_found
    })


def customer_details(request):
    combined_data = {}
    unique_emails = set()

    appointment_data = user_appointments.objects.all()

    for appointment in appointment_data:
        email_lower = appointment.name.lower()
        if email_lower not in unique_emails:
            unique_emails.add(email_lower)
            user = user_details.objects.filter(
                username__iexact=appointment.name).first()
            if user:
                combined_data[appointment.name.lower()] = {
                    'name': appointment.name.upper(),
                    'phone': appointment.phone,
                    'email': user.emailid,
                }

    return render(request, 'admin_dashboard/customer.html', {'combined_data': combined_data.values()})
