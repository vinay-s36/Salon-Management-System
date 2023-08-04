from django.shortcuts import render, redirect
from .models import ContactMessage, user_details


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
    # return render(request, 'contacts.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the form data to the database
        contact_message = ContactMessage(
            name=name, email=email, phone=phone, subject=subject, message=message)
        contact_message.save()

        # Redirect to the success page
        return redirect('contact_success')

    return render(request, 'contacts.html')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'admin_dashboard.html')


def admin_login(request):
    return render(request, 'login-admin.html')


def logincon(request):
    username = request.POST('username')
    password = request.POST('password')
    user = user_details.objects.get(username=username)
    if user.password == password:
        return redirect('/home')
    else:
        return redirect('/login')


def signup(request):
    username = request.POST('username')
    password = request.POST('password')
    email = request.POST('email')
    try:

        user = user_details.objects.get(username=username)
        lol = user_details(username=username, password=password, email=email)
        lol.save()
        print('saved')
        return redirect('/login')
    except:
        print('no')
        return redirect('/login')
