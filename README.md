# Image Classifier

This is a Restful MAchine learning API that makes use of pretrained TensorFlow Inception V3 model and Deeplearning to classify an image in matching classes out of 30 classes that contain human, different kinds of animals, objects like table, chair, aeroplanes, etc. Each user gets 6 tokens to start with and after his/her 6 transcations, he can either choose to discontinue his service or pay admin to refill his tokens. This API is deployed on AWS EC2 with host link "ec2-18-224-246-224.us-east-2.compute.amazonaws.com:5000/"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

you need to install

```
AWS 
Ubuntu
Python3, flask
Docker, Docker-compose
Postman
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests 
"
In your AWS virtual environment, go to your directory and run
 * sudo docker-compose build <br />
 * sudo docker-compose up <br />
 Once the API is running, copy the host url and paste it in post man, and give your command after /. In postman, <br />
 * register using a username and password on a POST protocol with /register URL <br />
 * copy the url of an image from internet and give it as an input along with username and password in POST protocol with /classify url <br />
 * Refill tokens using your usename, admin password and refill amount as the inputs to the api with POST protocol and /refill url <br />

  
  

## Deployment

Create a EC2 instance in AWS console, download the pep file and run the following commands:
> ssh -i <Pem file location><pem file name>.pem.txt <username>@<public dns of your instance>
 install socker and docker-compose
> mkdir <directory name>
> cd <directory name>
> git clone <your git link to the application containing docker-compose.yml>
> sudo docker-compose build
> sudo docker-compose up
 
 And voila! Your application is now hosted on AWS cloud.

## Acknowledgments

* Udemy
* El Farouk Yaseer
