from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Registerpage(request):
    return render(request,"app/Register.html")

def Loginpage(request):
    return render(request,"app/Login.html")

def RegisterUser(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        pwd = request.POST['passwd']

        slr = seller.objects.create(fname=fn,lname=ln,email=em,passwd=pwd) 

        return redirect("loginpage")
    else:
        msg = "Method Changes"
        return render(request,"app/Register.html",{'err':msg})
    
def loginuser(request):
    em = request.POST['email']
    pwd = request.POST['passwd']

    user = seller.objects.filter(email=em)
    if len(user) > 0:
        if user[0].passwd==pwd:
            return redirect("indexpage")
        else:
            msg = "password is incorrect"
            return render(request,"app/Login.html",{'err':msg})
    else:
        msg = "user not found"
        return render(request,"app/Login.html",{'err':msg}) 