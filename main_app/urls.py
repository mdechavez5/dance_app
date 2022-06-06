from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dancers/', views.DancerList.as_view(), name="dancer_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profile/', views.Profile.as_view(), name="profile"),
]