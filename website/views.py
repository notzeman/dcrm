from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout 
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {"records": records})
    

def login_user(request):
    print("VIEW CALLED")
    if request.method == 'POST':
        print("POST branch")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            print("LOGIN SUCCESS")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            print("LOGIN FAILED")
            return redirect('login')
    else:
        print("GET branch")
        return render(request, 'login.html', {"hide_navbar": True})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', { "hide_register": True, "form": form})
        return render(request, 'register.html', { "hide_register": True})
    else:
        form = SignUpForm()
        return render(request, 'register.html', { "hide_register": True, "form": form})

def update_record(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            record = Record.objects.get(id=id)
            record.first_name = request.POST['first_name']
            record.last_name = request.POST['last_name']
            record.email = request.POST['email']
            record.phone = request.POST['phone']
            record.address = request.POST['address']
            record.city = request.POST['city']
            record.state = request.POST['state']
            record.country = request.POST['country']
            record.zip_code = request.POST['zip_code']
            record.save()
            messages.success(request, 'You have successfully updated the record!')
            return redirect('home')
        record = Record.objects.get(id=id)
        return render(request, 'update_record.html', {"record": record})
    else:
        messages.error(request, 'You are not allowed to update this record!')
        return redirect('home')

def delete_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        record.delete()
        messages.success(request, 'You have successfully deleted the record!')
        return redirect('home')
    else:
        messages.error(request, 'You are not allowed to delete this record!')
        return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            record = Record.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                address = request.POST['address'],
                city = request.POST['city'],
                state = request.POST['state'],
                country = request.POST['country'],
                zip_code = request.POST['zip_code']
            )
            messages.success(request, 'You have successfully added the record!')
            return redirect('home')
        return render(request, 'add_record.html')
    else:
        messages.error(request, 'You are not allowed to add this record!')
        return redirect('home')