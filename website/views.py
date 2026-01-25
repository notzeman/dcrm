from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    

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
    return render(request, 'register.html', { "hide_register": True})
