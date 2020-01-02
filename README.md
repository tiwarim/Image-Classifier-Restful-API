# Image Classifier

This is a Restful MAchine learning API that makes use of pretrained TensorFlow Inception V3 model and Deeplearning to classify an image in matching classes out of 30 classes that contain human, different kinds of animals, objects like table, chair, aeroplanes, etc. Each user gets 6 tokens to start with and after his/her 6 transcations, he can either choose to discontinue his service or pay admin to refill his tokens. This API is deployed on AWS EC2 with host link "ec2-18-224-246-224.us-east-2.compute.amazonaws.com:5000/"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python3, flask
Docker, Docker-compose
Postman
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Python : 
https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html 
Flask:
https://pypi.org/project/Flask/ 
Docker 
https://docs.docker.com/docker-for-mac/install/ 
Docker-compose 
https://docs.docker.com/compose/install/. 
Postman:
https://www.getpostman.com/downloads/ 

```

### Resource Chart Protocol

```
| Resource      |      URL      | Protocol   | Parameters                     | status codes
| ------------- | ------------- | ---------  | -------------                  | ------------- 
| Register      | /register     | POST       | username, password             | 200 OK, 301 user exists
| Classify      | /classify     | POST       | username, password, image url  | 200 OK, 301 invalid user, 302 invalid password, 303 out of tokens
| Refill        | /refill       | POST       | username, password, refill amt | 200 OK, 301 invalid user, 302 invalid password, 304 wrong Admin password

```



## Running the tests
"
In your local machine, go to your project directory and run
 * sudo docker-compose build <br />
 * sudo docker-compose up <br />
 Once the API is running, copy the host url and paste it in post man, and give your command after /. In postman, <br />
 * register using a username and password on a POST protocol with /register URL <br />
 * copy the url of an image from internet and give it as an input along with username and password in POST protocol with /classify url <br />
 * Refill tokens using your usename, admin password and refill amount as the inputs to the api with POST protocol and /refill url <br />
 
 **Registration** <br />
<img width="450" height="350" alt="Screen Shot 2020-01-01 at 8 02 20 PM" src="https://user-images.githubusercontent.com/41305591/71648394-b2562b00-2cd1-11ea-94ed-02a81fa8d462.png">
 <br />
 **Classifying an image** <br />
 Given input: url for an image of dog <br />
 <img width="350" height="350" alt="Screen Shot 2020-01-01 at 7 55 30 PM" src="https://user-images.githubusercontent.com/41305591/71648275-afa70600-2cd0-11ea-946d-96553f48e1b5.png">
 
 <br />
 Output :
 <img width="550" height="400" alt="Screen Shot 2020-01-01 at 7 50 09 PM" src="https://user-images.githubusercontent.com/41305591/71648249-4921e800-2cd0-11ea-9fbe-7681295d2b1b.png">
 
 
 <br />
 Refilling tokens <br />
 <img width="450" height="350" alt="Screen Shot 2020-01-01 at 8 01 36 AM" src="https://user-images.githubusercontent.com/41305591/71648151-a026bd80-2cce-11ea-8ca1-3e6d72741bc0.png">


## Deployment

Create a EC2 instance in AWS console, download the pep file and run the following commands:  <br />
* ssh -i "Pem file location""pem file name".pem.txt "username"@"public dns of your instance"  <br />
 install docker and docker-compose.  <br />
* mkdir <directory name>.  <br />
* cd <directory name>
* git clone <your git link to the application containing docker-compose.yml>  <br />
* sudo docker-compose build <br />
* sudo docker-compose up. <br />
 
 Your application should now be up and running on AWS
 
## Acknowledgments

* Udemy
* El Farouk Yaseer
