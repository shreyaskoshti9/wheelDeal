from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, VehicleForm, LoginForm
from .models import Vehicle, Transaction
from django.core.mail import send_mail

def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['username'])
        form = LoginForm(request, data=request.POST)
        # print(form.cleaned_data['username'])
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
        else:
            print("error")        
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def list_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            return redirect('home')
    else:
        form = VehicleForm()
    return render(request, 'main/list_vehicle.html', {'form': form})

@login_required
def browse_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'main/browse_vehicles.html', {'vehicles': vehicles})

@login_required
def contact_owner(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(
            'Inquiry',
            message,
            request.user.email,
            [vehicle.owner.email]
        )
        return redirect('browse_vehicles')
    return render(request, 'main/contact_owner.html', {'vehicle': vehicle})
