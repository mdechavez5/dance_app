from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dancers/', views.DancerList.as_view(), name="dancer_list"),
    path('dancers/<int:pk>/', views.DancerDetail.as_view(), name="dancer_detail"),
    path('pieces/<int:pk>/new/', views.PieceCreate.as_view(), name="piece_create"),
    path('pieces/<int:pk>/update/',views.PieceUpdate.as_view(), name="piece_update"),
    path('pieces/<int:pk>/delete/',views.PieceDelete.as_view(), name="piece_delete"),
    path('pieces/<int:pk>',views.PieceDetail.as_view(), name="piece_detail"),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/',views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update',views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete/',views.PostDelete.as_view(), name="post_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profile/', views.Profile.as_view(), name="profile"),
]