from django.urls import path

from . import views

urlpatterns = [
    # path("login", views.loginPage, name="login"),
    path("register",views.register_user,name="register_user"),
    path('home', views.Home.as_view()),
]