
from django.urls import path
from amuapp import views

urlpatterns = [
    
    path('',views.home,name='home'),
]
