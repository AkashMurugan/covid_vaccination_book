# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from .models import VaccinationCentre, AppliedVaccination
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404
from django.db.models import Count


def home(request):
    return render(request, 'home.html')

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile')
        mpin = request.POST.get('mpin')
        try:
            user = User.objects.get(mobile_number=mobile_number)
            if user.check_password(mpin):
                login(request, user)
                return redirect('userdashboard')
            else:
                return render(request, 'login.html', {'error_message': 'Incorrect MPIN!'})
        except User.DoesNotExist:
            return redirect('signup')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        mpin = request.POST.get('mpin')
        confirm_mpin = request.POST.get('confirm_mpin')
        if mpin != confirm_mpin:
            return render(request, 'signup.html', {'error_message': 'MPINs do not match!'})
        if User.objects.filter(mobile_number=mobile_number).exists():
            error_message = 'User with the same mobile number already exists!'
            return render(request, 'signup.html', {'error_message': error_message})
        user = User.objects.create_user(username=mobile_number, mobile_number=mobile_number)
        user.set_password(mpin)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


@login_required(login_url='login')
def userdashboard_view(request):
    return render(request, 'userdashboard.html')


@login_required(login_url='login')
def admindashboard_view(request):
    return render(request, 'admindashboard.html')


def apply_view(request):
    available_centres = VaccinationCentre.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        age = request.POST['age']
        vaccination_date = request.POST['vaccination_date']
        vaccination_type = request.POST['vaccination_type']
        centre_id = request.POST['centre']
        vaccination_centre = VaccinationCentre.objects.get(id=centre_id)
        available_slots = vaccination_centre.available_slots()
        if available_slots > 0:
            applied_vaccination = AppliedVaccination(name=name, gender=gender, dob=dob, age=age, vaccination_date=vaccination_date, vaccination_type=vaccination_type, vaccination_centre=vaccination_centre)
            applied_vaccination.save()
            messages.success(request, 'Your vaccination slot has been successfully applied.')
            return redirect('apply')
        else:
            message = 'No available slots for the selected vaccination centre'
            return render(request, 'apply.html', {'centres': available_centres, 'message': message})
    return render(request, 'apply.html', {'centres': available_centres})


def admin_login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                return redirect('admindashboard')
            else:
                context["error"] = "You don't have sufficient privileges to access the admin page."
        else:
            context["error"] = "Invalid credentials. Please provide valid username and password."
    return render(request, 'admin_login.html', context)


def add_centre_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        working_hours = request.POST['working_hours']
        dosages_available = request.POST['dosages_available']
        centre = VaccinationCentre(name=name, location=location, working_hours=working_hours, dosages_available=dosages_available)
        centre.save()
        return render(request, 'add_centre.html')
    return render(request, 'add_centre.html')


def getvaccinationdetails_view(request):
    centres = AppliedVaccination.objects.all()
    return render(request, 'getvaccinationdetails.html', {'centres': centres})


def get_dosage_details_view(request):
    centres = VaccinationCentre.objects.all()
    return render(request, 'get_dosage_details.html', {'centres': centres})


def remove_centre_view(request):
    vaccination_centres = VaccinationCentre.objects.all()
    if request.method == 'POST':
        centre_id = request.POST['centre']
        centre = get_object_or_404(VaccinationCentre, id=centre_id)
        centre.delete()

    return render(request, 'remove_centre.html', {'centres': vaccination_centres})


def logout_view(request):
    auth.logout(request)
    return redirect('home')
