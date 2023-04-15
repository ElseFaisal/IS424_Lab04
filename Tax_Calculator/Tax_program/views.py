from django.shortcuts import render

# Create your views here.

def default(request):
    return render(request,'Tax_program/default.html')