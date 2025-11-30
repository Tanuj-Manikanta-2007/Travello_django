from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']
        if password1 == password2:
          if User.objects.filter(username = username).exists():
              messages.error(request, 'Username already taken!')
              return redirect("register")
          elif User.objects.filter(email = email).exists():
              messages.info(request,'email already exits  ')
              return redirect("register")
          else:
            user = User.objects.create_user(username = username,email = email,first_name = first_name,last_name = last_name,password = password1)
            user.save()
            return redirect("/login")
        
        else:
            messages.info(request,'password not match ')
            
            return redirect("register")
        
    else :
        return render(request, 'accounts/register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user =  auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials ')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")