from django.urls import path
from .import views

urlpatterns = [
      path('register/',views.register,name='register'),
      path('profile/', views.profile, name='profile'),
      path('profile/logout/register/',views.register, name='register'),
      path('logout/login/register/', views.register, name='register'),

]
