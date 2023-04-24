from django.urls import path
from . import views
urlpatterns = [
    path("",views.default,name="Defalut site"),
    path("taxrate",views.get_TaxRate,name="Get tax rate"),
    path("<int:price>",views.calculate_TotalPrice,name="Calculate total price")
]