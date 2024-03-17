import json
import logging
from channels.generic.websocket import WebsocketConsumer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from .models import *

logger = logging.getLogger(__name__)

class StationConsumer(WebsocketConsumer):
    def connect(self):
        # Get the sensor_id from the query parameters
        sensor_id = self.scope['query_string'].decode('utf-8')
        # Log the sensor_id
        logger.debug(f"Sensor ID: {sensor_id}")
        check = self.sensor_check(sensor_id)
        if check:
            #if check is successful, accept the connection
            self.accept()

            self.send(text_data=json.dumps({
                'type': 'Connection Established',
                'message': f'You are now connected! Sensor ID: {check.sensor_id}'
            }))
        else:
            #if check failed, reject the connection
            self.send(text_data=json.dumps({
                'type': 'Connection Failed',
                'message': f'Connection Rejected! Sensor ID does not exist!'
            }))
            self.close()

    def sensor_check(self, sensor_id):
        print(sensor_id)
        try:
            #update status to True
            Sensor.objects.filter(sensor_id=sensor_id).update(status=True)
            #to send back to connect() so connection is acceptable
            sensor = Sensor.objects.get(sensor_id=sensor_id)
            return sensor
        except Exception as e:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': f'{e}',
            }))
    
    #handle message
    def receive(self, text_data):
        sensor_id = self.scope['query_string'].decode('utf-8')
        message_data = json.loads(text_data)

        message_type = message_data['type']

        #perform action/function according to message type
        
        if message_type == 'print.message':
            print(message_data['content'])
        elif message_type == 'send.coordinate':
            self.handle_send_coordinate(sensor_id, message_data)

    def handle_print_message(message_data):
        print(message_data['content'])

    def handle_send_coordinate(self, sensor_id, message_data):
        try:
            latitude = message_data['latitude']
            longitude = message_data['longitude']
            Sensor.objects.filter(sensor_id=sensor_id).update(
                latitude=latitude,
                longitude=longitude
            )
            # Send success message back to the client
            self.send(text_data=json.dumps({
                'type': 'success',
                'message': 'Sensor data updated successfully',
            }))
        except Sensor.DoesNotExist:
            # Send an error response to the client
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Sensor not found',
            }))
        except Exception as e:
            # Send an error response to the client
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e),
            }))
    
    def disconnect(self, sensor_id):
        #update sensor status
        try:
            Sensor.objects.filter(sensor_id=sensor_id).update(status=False)
        except Exception as e:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e),
            }))
        print(f"Websocket disconnected with code: 1000")