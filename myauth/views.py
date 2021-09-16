from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from myauth.forms import SignUpForm,LoginForm
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate , login as auth_login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def signUp(request):
    if request.user.is_authenticated:
        return redirect("/")
    signup_form = SignUpForm()
    if request.method == "POST":
        signup_form  = SignUpForm(request.POST)
        if signup_form.is_valid() and signup_form.cleaned_data["password"] == signup_form.cleaned_data["password_confirm"]:
            # signup_form.save()
            password = signup_form.cleaned_data["password"]
            first_name = signup_form.cleaned_data["first_name"]
            last_name = signup_form.cleaned_data["last_name"]
            username = signup_form.cleaned_data["username"]
            email = signup_form.cleaned_data["email"]

            # using create user method
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            messages.success(request,"Welcome to our site")
            messages.success(request,"Thanks for signing up")
            return redirect("/")
        elif signup_form.cleaned_data["password"] != signup_form.cleaned_data["password_confirm"] :
            signup_form.add_error("password_confirm","Password do not match")

    context = {
        "form" : signup_form 
    }
    return render(request,"myauth/signup.html",context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = LoginForm()
    if request.method == "POST":
        login_form  = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                messages.info(request,"You are logged in succesfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")

    context = {
        "form" : login_form 
    }
    return render(request,"myauth/login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("/")