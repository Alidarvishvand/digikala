from django.shortcuts import render,HttpResponse




def hello_world(request):
    return render(request,'index.html')