"""Views module stores all the views of the application"""
import json
from shortner.new_view import NewView
from shortner.stub_view import StubView
from shortner.delete_view import DeleteView
from shortner.list_view import ListUrlsView
from shortner.update_view import UpdateView
from shortner.custom_view import CustomView
from shortner.stats_view import StatsView
from shortner.login import login_test

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

__all__ = ["NewView", "StubView", "UpdateView", "DeleteView", "ListUrlsView", "login_test", "CustomView", "StatsView"]

def home(request):
    print("hitting home")
    return render(request, "authentication/index.html")


def signup(request):
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        # requestJsonBody = json.loads(request)
        uservalue = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]

        if User.objects.filter(username=uservalue).exists():
            messages.error(request, "Username is already taken")
        elif User.objects.filter(email = email).exists():
            messages.error(request, "Email is already used")
        elif len(email) < 4:
            messages.error(request, "Email must be greater than 3 characters.")
        elif len(fname) < 2:
            messages.error(request, "First name must be greater than 1 character.")
        elif len(lname) < 2:
            messages.error(request, "Last name must be greater than 1 character.")
        elif password1 != password2:
            messages.error(request, "Passwords don't match.")
        elif len(password1) < 5:
            messages.error(request, "Password must be at least 5 characters.")
        else:
            myuser = User.objects.create_user(uservalue,email,password1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()
            messages.success(request, "Your Account has been successfully created.")
            request.session['username'] = uservalue
            return redirect("home")
    return render(request, "authentication/signup.html")

def signin(request):

    # Only through forms
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name
            request.session['username'] = username
            return redirect("homepage",fname=fname)
        else:
            messages.error(request,"Bad Credentials!")
            return redirect("home")

    # Render the main page if we try to access signin through the url (GET)
    return render(request, "authentication/index.html")


def homepage(request, fname):
    if(request.method == 'GET'):
       messages.success(request, "Login Successfull!")
       print("{} has logged in".format(fname))
       args = {}
       args['userFname'] = fname
       return render(request, 'homepages/index.html', args)



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect("home")
