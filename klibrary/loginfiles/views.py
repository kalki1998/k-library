from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib import messages
# Create your views here.

def signup(request):
        if request.method == 'POST':
             username = request.POST['username']
             firstname = request.POST['firstname']
             lastname = request.POST['lastname']
             email = request.POST['email']
             password = request.POST['password']
             repassword = request.POST['repassword']
             myuser = User.objects.create_user(username,email,password)
             myuser.f_name = firstname
             myuser.l_name = lastname 
             myuser.save()
             messages.success(request,'your account created successfully.')
             return redirect('login')
        
        return render(request,'loginpage/signup.html')

def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = authenticate(username=username,password=password)

         if user is not None:
              auth_login(request, user)
              f_name = user.first_name
              return render(request,'index/home.html', {'fname': f_name})

         else:
            messages.error(request, 'bad credentials!')
            return redirect('home')
    return render(request, 'loginpage/signin.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'logged out successfully.')
    return redirect('home')
