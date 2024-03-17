from django.urls import path
from . import views
from .views import LocationViewset, StationViewset, SensorViewset
from rest_framework.routers import DefaultRouter
#default route just in case we will be creating new views later on
urlpatterns = [
    path('location/count/', LocationViewset.as_view({'get': 'count'}), name='location-count'),
    path('station/count/', StationViewset.as_view({'get': 'count'}), name='location-count'),
    path('sensor/count/', SensorViewset.as_view({'get': 'count'}), name='location-count'),
]
router = DefaultRouter()
#register all viewset into urlpatterns, this would generate url automatically
router.register('location', views.LocationViewset, basename='location')
router.register('station', views.StationViewset, basename='station')
router.register('sensor', views.SensorViewset, basename='sensor')
urlpatterns += router.urls