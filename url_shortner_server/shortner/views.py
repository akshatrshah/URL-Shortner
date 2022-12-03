"""Views module stores all the views of the application"""
import json
from shortner.new_view import NewView
from shortner.stub_view import StubView
from shortner.delete_view import DeleteView
from shortner.list_view import ListUrlsView
from shortner.update_view import UpdateView
from shortner.custom_view import CustomView
from shortner.login import login_test

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

__all__ = ["NewView", "StubView", "UpdateView", "DeleteView", "ListUrlsView", "login_test", "CustomView"]

def home(request):
    print("hitting home")
    return render(request, "authentication/index.html")


def signup(request):
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        # requestJsonBody = json.loads(request)
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your Account has been successfully created.")
        request.session['username'] = username
        return redirect("home")
    return render(request, "authentication/signup.html")

def signin(request):

    # Only through forms
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]
        import pdb; pdb.set_trace()
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
