from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('send_login_email/', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
]
