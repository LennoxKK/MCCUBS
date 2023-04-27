from django.urls import path
from User.views import register,_export_,profile,user_profile,create_profile,view_profile
from django.contrib.auth import views as auth_views



app_name = 'Users'

urlpatterns = [
    path('register/', register, name ='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<str:username>', user_profile, name='profile'),
    path('create_profile/', create_profile, name='user_profile'),
    path('profile/<str:first_name>/', view_profile, name='view'),
    path('_export_/',_export_,name='download'),
]




