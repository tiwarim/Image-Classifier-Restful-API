# Image Classifier

This is a Restful MAchine learning API that makes use of pretrained TensorFlow Inception V3 model and Deeplearning to classify an image in matching classes out of 30 classes that contain human, different kinds of animals, objects like table, chair, aeroplanes, etc. Each user gets 6 tokens to start with and after his/her 6 transcations, he can either choose to discontinue his service or pay admin to refill his tokens. This API is deployed on AWS EC2 with host link "ec2-18-224-246-224.us-east-2.compute.amazonaws.com:5000/"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For development, you need to have

```
Text editor
AWS 
Ubuntu
Docker and Docker-compose

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
 > sudo docker-compose build 
 > sudo docker-compose up
 Once the API is running, copy the host url and paste it in post man, and give your command after /. In postman, 
 > register using a username and password on a POST protocol with /register URL
 <img width="521" height = "400" alt="Screen Shot 2020-01-01 at 5 25 04 AM" src="https://user-images.githubusercontent.com/41305591/71640419-90b85d80-2c57-11ea-838b-1386055273cb.png">


### Break down into end to end tests

Explain what these tests test and why
 
```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Contributor Covenant](https://www.contributor-covenant.org/) - Used for the Code of Conduct
* [Creative Commons](https://creativecommons.org/) - Used to choose the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors) who participated in this project.

## License

This project is licensed under the [Attribution 4.0 International](LICENSE.md) Creative Commons License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
