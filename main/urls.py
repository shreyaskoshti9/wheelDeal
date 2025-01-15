from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('list_vehicle/', views.list_vehicle, name='list_vehicle'),
    path('browse_vehicles/', views.browse_vehicles, name='browse_vehicles'),
    path('contact_owner/<int:vehicle_id>/', views.contact_owner, name='contact_owner'),
]
