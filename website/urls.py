from django.urls import path
from . import views

urlpatterns = [
    path('', views.website, name = 'website-home'),
    path('website/', views.website, name = 'website-home'),
    path('weather/', views.weather, name = 'website-weather'),
    path('final/', views.final, name = 'website-final'),
    path('api1/', views.final, name = 'website-api1'),
    path('api2/', views.final, name = 'website-api2'),
    path('api3/', views.final, name = 'website-api3'),
    path('api4/', views.final, name = 'website-api4'),
    path('api5/', views.final, name = 'website-api5'),
]

