from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Inbuilt Admin Panel
    path('admin/', admin.site.urls),
    # Main App Route
    path('',include('Todo.urls',namespace='todo')),
    # Users Route
    path('auth1/',include('auth1.urls')),
    # API Route
    path('api/',include('Todo_api.urls')),
    path('rest_auth/',include('rest_auth.urls')),

    # Password Change links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    # Password Reset links
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]