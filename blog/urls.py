from django.urls import path, include
from .views import *

urlpatterns = [
    # path('accounts/', include("django.contrib.auth.urls")),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
    path('profile/', profile, name='profile'),
    # path('signput/', signout, name='signout'),
    path('signout/', signout, name='signout'),  
    
]