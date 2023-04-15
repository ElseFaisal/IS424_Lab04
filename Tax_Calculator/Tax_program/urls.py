from django.urls import path
from . import views
urlpatterns = [
    path("",views.default,name="Defalut site"),
    path("<float:price>",views.calculate_TotalPrice,name="Calculate total price")
]