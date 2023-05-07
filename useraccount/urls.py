from django.urls import path

from useraccount.views import userlogin,userlogout

app_name='useraccount'
urlpatterns = [
    path('login/',userlogin,name='userlogin'),
    path('logout/',userlogout,name='userlogout'),
]
