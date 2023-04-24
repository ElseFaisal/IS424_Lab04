from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

TAX_RATE = 0.15

def default(request):
    return render(request,'Tax_program/default.html')

def calculate_TotalPrice(request,price):
    return render(request,'Tax_program/calcTotPrice.html',{"price":(price*(1+TAX_RATE))})
    

def get_TaxRate(request):
    return render(request,'Tax_program/getTaxRate.html',{"tax":(TAX_RATE*100)})