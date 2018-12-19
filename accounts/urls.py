from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('send_email/', views.send_login_email, name='send_login_email'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
