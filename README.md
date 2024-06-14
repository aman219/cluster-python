# cluster
### A backend for web NAS (Network Attached Server) written in python. It use Django framework as backend for managing server resources.

## Dependencies 
1. [Cluster front](https://github.com/aman219/cluster-front).
2. ffmpeg

## Steps to run server :-

```
python -m venv env
```

```
source env/bin/activate
```
 
 ### To install all reqirements.
 ```
 pip install -r reqirement.txt
 ```
 ### To start the devlopment server.
 ```
 python manage.py runserver
 ```
 ### To start devlopment server in LAN.
 ```
 python manage.py runserver 0.0.0.0:8000
 
 ```
