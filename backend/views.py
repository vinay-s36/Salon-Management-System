from django.shortcuts import render


def landing(request):
    return render(request, 'landing-page.html')


def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def appointments(request):
    return render(request, 'appointments.html')


def contacts(request):
    return render(request, 'contacts.html')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'admin_dashboard.html')


def admin_login(request):
    return render(request, 'login-admin.html')
