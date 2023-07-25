# docker-exercise

exercise 1: Flask, gunicorn and Nginx to create a load balancer web server
To build and scale your number of environment use this line
> docker-compose up -d --build --scale app=3 

exercise 2: Flask and HaProxy to create a load balance web server
The web server has two endpoint /cpu_xx /ram_xx_xx in order to do a stress test with python's library psUtil

exercise 3: Flask, Haproxy and locust
Does the same thing of exercise 2 , additionally it use locust library to run stress test and generate a report.
Frontend runs on port 80 , locust page on 8089
To run use these commands:
> docker-compose up --build
> locust -f locustfile.py
