from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 


def registerform(request):
    if request.method == 'POST':
        username = request.POST['uname'] 
        email = request.POST['email']
        password = request.POST['pass1']
        cnfpassword = request.POST['pass2']

        if password == cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists!")
                return render(request,"result.html")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                messages.info(request,"User Saved!")
                return render(request,"result.html")
        else:
                messages.info(request,"Password does'nt match!")
                return render(request,"result.html")
    else:
        return render(request,"register.html")


def userslist(request):
    Users = User.objects.all()
    return render(request,"read.html",{'Users':Users})




def delete(request,id):

    Del = User.objects.filter(pk=id)
    Del.delete()
    return HttpResponse('User Data Deleted:(')



