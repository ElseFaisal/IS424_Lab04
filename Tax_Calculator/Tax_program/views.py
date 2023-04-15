from django.shortcuts import render

# Create your views here.

TAX_RATE = 0.15

def default(request):
    return render(request,'Tax_program/default.html')

def calculate_TotalPrice(request,price):
    return render(request,'Tax_program/calcTotPrice.html',{"price":(price*(1+TAX_RATE))})