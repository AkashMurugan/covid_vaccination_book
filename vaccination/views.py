# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import VaccinationCentre, AppliedVaccination, VaccinationSlot
from .models import VaccinationRegistration
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        # Process login form data
        mobile_number = request.POST.get('mobile')
        mpin = request.POST.get('mpin')

        try:
            user = User.objects.get(mobile_number=mobile_number)
            if user.check_password(mpin):
                login(request, user)
                return redirect('userdashboard')
            else:
                # If the MPIN is incorrect, display an error message
                return render(request, 'login.html', {'error_message': 'Incorrect MPIN!'})
        except User.DoesNotExist:
            return redirect('signup')

    return render(request, 'login.html')




def signup_view(request):
    if request.method == 'POST':
        # Process signup form data
        mobile_number = request.POST.get('mobile_number')
        mpin = request.POST.get('mpin')
        confirm_mpin = request.POST.get('confirm_mpin')

        # Perform validation
        if mpin != confirm_mpin:
            # If MPIN and Confirm MPIN do not match, display an error message
            return render(request, 'signup.html', {'error_message': 'MPINs do not match!'})

        # Check if a user with the same mobile number already exists
        if User.objects.filter(mobile_number=mobile_number).exists():
            # If a user with the same mobile number exists, display an error message
            error_message = 'User with the same mobile number already exists!'
            return render(request, 'signup.html', {'error_message': error_message})

        # Create a new user
        user = User.objects.create_user(username=mobile_number, mobile_number=mobile_number)
        user.set_password(mpin)  # Set the MPIN as the user's password

        # Save the user to the database
        user.save()

        return redirect('login')

    return render(request, 'signup.html')


@login_required(login_url='login')
def userdashboard_view(request):
    return render(request, 'userdashboard.html')



@login_required(login_url='login')
def admindashboard_view(request):
    return render(request, 'admindashboard.html')


@login_required(login_url='login')
def registervaccination_view(request):
    user = request.user
    registrations = VaccinationRegistration.objects.filter(user=user)
    error_message = ""

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        dob = request.POST['dob']

        # Check if the user has already registered 4 members
        if registrations.count() >= 1:
            # Display an error message or handle the case where the limit is reached
            error_message = "You have already registered 1 member. Cannot add more."
            # You can add this error_message to the context and display it in the template

        else:
            registration = VaccinationRegistration(user=user, name=name, gender=gender, age=age, dob=dob)
            registration.save()

        registrations = VaccinationRegistration.objects.filter(user=user)

    context = {'registrations': registrations, 'error_message': error_message}
    return render(request, 'registervaccination.html', context)



def apply_view(request):
    available_centres = VaccinationCentre.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        centre_id = request.POST['centre']
        vaccination_centre = VaccinationCentre.objects.get(id=centre_id)

        # Calculate the available slots for the vaccination centre
        available_slots = vaccination_centre.available_slots()

        if available_slots > 0:
            # Create a new instance of AppliedVaccination
            applied_vaccination = AppliedVaccination(name=name, age=age, vaccination_centre=vaccination_centre)
            applied_vaccination.save()

            # Redirect to a success page or another URL
            return redirect('home')
        else:
            message = 'No available slots for the selected vaccination centre'
            return render(request, 'apply.html', {'centres': available_centres, 'message': message})

    return render(request, 'apply.html', {'centres': available_centres})


def admin_login_view(request):
    if request.method == 'POST':
        # Process admin login form data
        username = request.POST['username']
        password = request.POST['password']
        # Perform admin authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='admin').exists():
                auth.login(request, user)
                return redirect('admindashboard')
        else:
            # Handle invalid admin credentials
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')



def add_centre_view(request):
    if request.method == 'POST':
        # Process add centre form data
        name = request.POST['name']
        location = request.POST['location']
        working_hours = request.POST['working_hours']
        dosages_available = request.POST['dosages_available']

        centre = VaccinationCentre(name=name, location=location, working_hours=working_hours, dosages_available=dosages_available)
        centre.save()
        # Create a new VaccinationCentre object and save it to the database
        return render(request, 'add_centre.html')
    return render(request, 'add_centre.html')

def get_dosage_details_view(request):
    # Retrieve dosage details grouped by centres
    #dosage_details = VaccinationCentre.objects.values('name').annotate(total_dosages=Count('dosage'))
    #centres = VaccinationCentre.objects.annotate(total_dosage=Sum('dosage')).values('name', 'location', 'total_dosage')
    centres = VaccinationCentre.objects.all()

    return render(request, 'get_dosage_details.html', {'centres': centres})
    #return render(request, 'get_dosage_details.html', {'get_dosage_details': dosage_details})

def remove_centre_view(request):
    vaccination_centres = VaccinationCentre.objects.all()
    if request.method == 'POST':
        # Process remove centre form data
        centre_id = request.POST['centre']
        centre = get_object_or_404(VaccinationCentre, id=centre_id)
        centre.delete()
        # Delete the VaccinationCentre object with the specified ID from the database

    return render(request, 'remove_centre.html', {'centres': vaccination_centres})

def logout_view(request):
    auth.logout(request)
    return redirect('home')
