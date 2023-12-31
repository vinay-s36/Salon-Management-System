"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backendapp.views import contacts, about, services, appointments, home, login, landing, dashboard, admin_login, signup, display_all, logincon, adminsignin, new, rejected, accepted, search_appointment, search_invoice, invoice, appointment_details, search_appointment1, spcl_service, customer_details, qrcode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts', contacts),
    path('special-service', spcl_service),
    path('admin-dashboard/customers', customer_details),
    path('asignin', adminsignin),
    path('signup', signup),
    path('signin', logincon),
    path('services', services),
    path('about-us', about),
    path('qr-code', qrcode),
    path('appointments', appointments),
    path('appointment-details', appointment_details),
    path('home', home),
    path('login', login),
    path('admin-dashboard', dashboard),
    path('admin-dashboard/all-appointments', display_all),
    path('admin-dashboard/new-appointments', new),
    path('admin-dashboard/accepted-appointments', accepted),
    path('admin-dashboard/rejected-appointments', rejected),
    path('admin-dashboard/invoices', invoice),
    path('admin-dashboard/search-invoice', search_invoice),
    path('admin-dashboard/search-appointment', search_appointment),
    path('search-app-num', search_appointment1),
    path('admin-login', admin_login),
    path('', landing),
]
