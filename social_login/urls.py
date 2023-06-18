from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("", views.LoginPageView.as_view(), name="login_page"),
    path("success/", views.LoginSuccessView.as_view(), name="login_success"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
