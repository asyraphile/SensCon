from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('location/', views.LocationViewSet.as_view(), name='locations'),
]