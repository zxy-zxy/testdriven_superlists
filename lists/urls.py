from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('new/', views.new_list, name='new_list'),
    path('new/', views.new_list2, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
