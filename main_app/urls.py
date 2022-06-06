from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dancers/', views.DancerList.as_view(), name="dancer_list.html"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]