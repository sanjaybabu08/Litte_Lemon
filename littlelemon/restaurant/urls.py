from django.contrib import admin 
from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    #path('', views.sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    
    #path('booking/', bookingview.as_view()),
]