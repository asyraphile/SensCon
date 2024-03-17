from django.db import models
import uuid

# Create your models here.
    
class Location(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Name")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
class Station(models.Model):
    station_id = models.CharField(max_length=50, unique=True, editable=False, verbose_name="Station Id")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Location")
    status = models.BooleanField(default=False, verbose_name="Status") #False = OFF, True = ON
    number_of_devices = models.IntegerField(default=0, verbose_name="Number of Devices")
    last_connection_time = models.DateTimeField(verbose_name="Last Connection Time")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.station_id

    #Station ID generator
    def save(self, *args, **kwargs):
        #save the new station
        super().save(*args, **kwargs)
        #if station has no id, it would create a new station_id
        if not self.station_id:
            self.station_id = "STID%05d" % self.id
            self.save()
        return "STID%05d"% self.id
    
class Sensor(models.Model):
    sensor_id = models.CharField(max_length=50, unique=True, editable=False, verbose_name="Sensor Id")
    station = models.ForeignKey(Station, to_field="station_id", on_delete=models.CASCADE, verbose_name="Station")
    status = models.BooleanField(default=False, verbose_name="Status") #False = OFF, True = ON
    latitude = models.FloatField(default=0,verbose_name="Latitude")
    longitude = models.FloatField(default=0,verbose_name="Longitude")
    last_connection_time = models.DateTimeField(verbose_name="Last Connection Time")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.sensor_id

    #Sensor ID generator
    def save(self, *args, **kwargs):
        #save the new station
        super().save(*args, **kwargs)
        #if sensor has no id, it would create a new sensor_id
        if not self.sensor_id:
            self.sensor_id = "SID%05d" % self.id
            self.save()
        return "SID%05d"% self.id
         