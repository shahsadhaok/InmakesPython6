from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CustomOrder
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')



def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not username or not password or not cpassword:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Account created successfully. You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

    return render(request, "register.html")
def logout(request):
   auth.logout(request)
   return redirect('/')

def new_page(request):
    return render(request, 'new_page.html')

def form_view(request):
    message = None
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        department_id = request.POST['department_id']
        course_id = request.POST['course_id']
        purpose = request.POST['purpose']
        materials_provide = ', '.join(request.POST.getlist('materials_provide'))
        message = "Form submitted successfully!"

        form = CustomOrder.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            department_id=department_id,
            course_id=course_id,
            purpose=purpose,
            materials_provide=materials_provide
        )
    return render(request, 'form.html', {'message': message})
