
# SensCon
An iOT management system that handles sensors from multiple stations in multiple locations.




## Acknowledgements

 - [Installation](#Installation)
 - [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Python 3.8 and above installed on your computer.
2. Open command prompt in this directory and create virtual environment by running "python -m venv venv".
3. Once venv is created, run ".\venv\Scripts\activate" to activate the virtual environment.
4. Run "python manage.py runserver" to start the server.

In order to login into admin, you either create a new admin account by running python manage.py createsuperuser or browse to "http://localhost:8000/admin/" with username and password as Admin, User@123.


## API Endpoints

1. http://localhost:8000/api/location/ on GET,POST,PUT,DELETE
2. http://localhost:8000/api/station/ on GET,POST,PUT,DELETE
3. http://localhost:8000/api/sensor/ on GET,POST,PUT,DELETE
4. http://localhost:8000/api/location/count/
5. http://localhost:8000/api/station/count/
6. http://localhost:8000/api/sensor/count/
7. ws://localhost:8000/ws/connect-server/ for websocket


Instruction to use the websocket to connect/ping the server
1. Use the endpoint no. 7 and include sensor id at the end of it. For example: ws://localhost:8000/ws/connect-server/<sensor_id>
2. Send message in json for there are two functions built with websocket:
    i. Print Message 
    {
        "type": "print.message",
        "content": "Your message"
    }
    ii. Send Coordinate
    {
        "type": "send.coordinate",
        "latitude": "your latitude",
        "longitude": "your longitude
    }


The system is incomplete, so in order to run the user interface you will have to navigate to "UI\material-dashboard-master\pages" and open dashboard.html.
I didn't run the UI together in Django because my plan was to build a standalone backend and frontend server.