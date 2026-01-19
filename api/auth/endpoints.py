from django.urls import path
from .generic_api import (
    LoginView,
    RegisterView,
    LogoutView,
    ProfileView,
    ChangePasswordView,
    ResetPasswordConfirmView,
    ResetPasswordRequestView,
    ResetPasswordVerifyView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/request/', ResetPasswordRequestView.as_view(), name='reset-password-request'),
    path('reset-password/verify/', ResetPasswordVerifyView.as_view(), name='reset-password-verify'),
    path('reset-password/confirm/', ResetPasswordConfirmView.as_view(), name='reset-password-confirm'),
]