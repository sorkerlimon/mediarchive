from django.urls import path
from .views import profile,loginUser,logoutUser,registerUser

urlpatterns = [
    path('',profile,name='profile'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
]