from django.urls import path
from .views import   login1, logout1,register,phonenum,viewphone,logout1


urlpatterns=[
    path('register/',register,name='register'),
    path('login/',login1,name='login'),
    path('addphone/',phonenum,name='add'),
    path('viewphone/',viewphone,name='view'),
    path('logout/',logout1,name='logout' ),
    
    

]