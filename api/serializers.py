from rest_framework import serializers
from .models import *

#Serializers are going to help us align the incoming and outgoing data into the format, so we have to state the characteristics to be displayed/edited into fields

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('station_id', 'location', 'status', 'number_of_devices', 'last_connection_time')

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('sensor_id', 'station', 'status', 'latitude', 'longitude', 'last_connection_time')