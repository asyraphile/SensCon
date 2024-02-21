from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
#import all serializers
from .serializers import *
from .models import *
# Create your views here.

class LocationViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Location.objects.all() # this is equal to SQL query select * from Location
    serializer_class = LocationSerializer

    def list(self, request):
        queryset = self.queryset
        try:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            response_data = {
                'message': 'Location listing failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {
                'message': 'Location created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'message': 'Location create failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        
        try:
            queryset = self.queryset.filter(pk=pk).first()
            serializer = self.serializer_class(queryset, many=False)
            print("HERE")
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            response_data = {
                'message': 'Location retrieve failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            #get data from keyword arguments
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            #validate through the serializer created
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                'message': 'Location updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Location update failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.queryset
        try:
            queryset.filter(pk=pk).delete()
            response_data = {
                'message': 'Location deleted successfully',
                'data': ''
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Location delete failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    def count(self, request):
        queryset = self.queryset
        try:
            total = queryset.count()
            response_data = {
                'message': 'Location count successfully',
                'data': total
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'message': 'Location count failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class StationViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Station.objects.all() # this is equal to SQL query select * from Location
    serializer_class = StationSerializer

    def list(self, request):
        queryset = self.queryset
        try:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            response_data = {
                'message': 'Station listing failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {
                'message': 'Station created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'message': 'Station create failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            queryset = self.queryset.filter(pk=pk).first()
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception as e:
            response_data = {
                'message': 'Station retrieve failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            #get data from keyword arguments
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            #validate through the serializer created
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                'message': 'Station updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Station update failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.queryset
        try:
            queryset.filter(pk=pk).delete()
            response_data = {
                'message': 'Station deleted successfully',
                'data': ''
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Station delete failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    def count(self, request):
        queryset = self.queryset
        try:
            total = queryset.count()
            response_data = {
                'message': 'Station count successfully',
                'data': total
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'message': 'Station count failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
class SensorViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Sensor.objects.all() # this is equal to SQL query select * from Location
    serializer_class = SensorSerializer

    def list(self, request):
        queryset = self.queryset
        try:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            response_data = {
                'message': 'Sensor listing failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {
                'message': 'Sensor created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'message': 'Sensor create failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            queryset = self.queryset.filter(pk=pk).first()
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception as e:
            response_data = {
                'message': 'Sensor retrieve failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            #get data from keyword arguments
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            #validate through the serializer created
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                'message': 'Sensor updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Sensor update failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.queryset
        try:
            queryset.filter(pk=pk).delete()
            response_data = {
                'message': 'Sensor deleted successfully',
                'data': ''
            }
            return Response(response_data)
        #Handle exception
        except Exception as e:
            response_data = {
                'message': 'Sensor delete failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
    def count(self, request):
        queryset = self.queryset
        try:
            total = queryset.count()
            response_data = {
                'message': 'Sensor count successfully',
                'data': total
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'message': 'Sensor count failed',
                'data': f'{e}'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)