from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView

urlpatterns = [
# User Related Operations
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]