from django.shortcuts import render, redirect
from .models import Farmer
from django.contrib.auth.models import User
from crops.models import Crop
from products.models import Medicine
from history.models import DetectionHistory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Register View
def register(request):

    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Debug print (temporary)
    

        # Validation
        if not name or not email or not password:
            return render(request,'users/register.html',{
                'error':'All fields required'
            })

        # Check duplicate
        if User.objects.filter(username=email).exists():
            return render(request,'users/register.html',{
                'error':'Email already registered'
            })

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Create farmer
        Farmer.objects.create(
            user=user,
            name=name,
            email=email
        )

        return redirect('login')

    return render(request,'users/register.html')
# Login View
def login_view(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'users/login.html')


# Dashboard
@login_required
def dashboard(request):

    crops = Crop.objects.count()
    medicines = Medicine.objects.count()
    detections = DetectionHistory.objects.filter(
        user=request.user
    ).count()

    context = {
        'crops': crops,
        'medicines': medicines,
        'detections': detections
    }

    return render(request, 'dashboard.html', context)


# Profile
@login_required
def profile(request):

    farmer, created = Farmer.objects.get_or_create(
        user=request.user,
        defaults={
            'name': request.user.username,
            'email': request.user.email
        }
    )

    crops = Crop.objects.count()
    detections = DetectionHistory.objects.filter(user=request.user).count()
    medicines = Medicine.objects.count()

    return render(request,'users/profile.html',{
        'farmer': farmer,
        'crops': crops,
        'detections': detections,
        'medicines': medicines
    })

# Admin Dashboard
def admin_dashboard(request):

    farmers = User.objects.count()
    crops = Crop.objects.count()
    medicines = Medicine.objects.count()
    diseases = DetectionHistory.objects.count()

    context = {
        'farmers': farmers,
        'crops': crops,
        'medicines': medicines,
        'diseases': diseases
    }

    return render(request,'users/admin_dashboard.html',context)


# Logout
def logout_view(request):
    logout(request)
    return redirect('/')


# Edit Profile
@login_required
def edit_profile(request):

    farmer, created = Farmer.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        farmer.name = request.POST.get('name')
        farmer.email = request.POST.get('email')
        farmer.phone = request.POST.get('phone')
        farmer.location = request.POST.get('location')
        farmer.soil_type = request.POST.get('soil_type')

        if request.FILES.get('profile_pic'):
            farmer.profile_pic = request.FILES.get('profile_pic')

        farmer.save()

        return redirect('profile')

    return render(request,'users/edit_profile.html',{
        'farmer': farmer
    })