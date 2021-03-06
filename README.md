# django-microservices
Django Microservices Project using Docker, nginx and Django REST Framework

Overview
--------
We have 3 docker containers:

* polls: runs the polls service
* questions: runs the questions service
* votes: runs the votes service

Requirements
------------
* docker
* docker-compose

Usage
-----

    $ docker-compose up

Configuration
-------------
Configuration is handled by environment variables, for development purpose you just need to update / add entries in .env file for each service.

Endpoints
--------
to run project services endpoints:
* polls endpints under: http://127.0.0.1:8001/docs/
* questions endpints under: http://127.0.0.1:8002/docs/
* votes endpints under: http://127.0.0.1:8003/docs/

to add a superuser for any service:

    $ docker-compose run <container_name> sh -c "python <container_folder>/manage.py createsuperuser"