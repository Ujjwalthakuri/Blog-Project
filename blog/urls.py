from django.urls import path, include
from .views import *

urlpatterns = [
    # path('accounts/', include("django.contrib.auth.urls")),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
    path('profile/', profile, name='profile'),
    path('postdetail/<int:pk>/', post_detail, name='postdetail'),
    path('postedit/<int:pk>/', post_edit, name='postedit'),
    path('postdel/<int:pk>/', post_del, name='postdel'),
    path('signout/', signout, name='signout'),  
    
]