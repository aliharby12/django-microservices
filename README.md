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

* polls endpints under: http://0.0.0.0:8001/docs
* questions endpints under: http://0.0.0.0:8002/docs
* votes endpints under: http://0.0.0.0:8003/docs