from django.shortcuts import render

# Create your views here.

def pare(request):
    return render(request,'pare.html')

def child(request):
    return render(request,'child.html')    