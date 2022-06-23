from django.shortcuts import render,redirect

from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request=="POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        mail = request.POST['mail']
        user=User.objects.create_user(username=username,password1=password2,mail=mail,firstname=firstname,lastname=lastname)
        user.save();
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')

