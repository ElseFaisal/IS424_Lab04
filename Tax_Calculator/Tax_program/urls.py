from django.urls import path
from . import views
urlpatterns = [
    path("",views.default,name="Defalut site")
]