from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
    path('profile/', profile, name='profile'),
    path('postdetail/<int:pk>/', post_detail, name='postdetail'),
    path('postedit/<int:pk>/', post_edit, name='postedit'),
    path('postdel/<int:pk>/', post_del, name='postdel'),
    path('signout/', signout, name='signout'),  
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='base_cont/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='base_cont/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='base_cont/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complet/', auth_view.PasswordResetCompleteView.as_view(template_name='base_cont/password_reset_complete.html'), name='password_reset_complete'),
    # blog/urls.py
    path('search/', search_posts, name='search_posts'),

]
