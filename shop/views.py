from django.shortcuts import render,HttpResponse,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def hello_world(request):
    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('Welcome'))
            return redirect('shop:shop')
        else:
            messages.error(request,('Invalid username or password'))
            return redirect('shop:login')
    else:
         
         return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('you are logged out'))
    return redirect('shop:shop')