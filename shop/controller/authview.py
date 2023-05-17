from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from shop.forms import CustomUserForm


def register(request):
    form = CustomUserForm()
    if request.method == "POST": 
        if request.POST.get('register') == 'submit':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('register')  
        elif request.POST.get('login') == 'Login':
            username1 = request.POST.get('sign_username')
            password1 = request.POST.get('sign_password')
            user=authenticate(request,username=username1,password=password1)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return redirect('register')
    context = {'form':form}
    return render(request,"index.html",context)
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/register")
    
