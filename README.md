# Rap Name Generator

### Resources

* Trello - https://trello.com/b/dCUsyGNg/rap-name-generator
* Website - http://35.242.143.43:5000

## Contents 

* Brief
  * Minimum Requirements
* Functionality
* Data
* Tech Stack
* CI Pipeline 
* Testing 
* Front-End Design
* Risk Assessment
* Difficulties
* Current Issues
* Future Improvements
* Authors

## Brief

The brief for this project can be outlined as creating an application that generates an output upon a set of predefined rules.

### Minimum requirements

The minimum requirments expected to meet this brief are as follows:

* Kanban board with full expansion on tasks needed to complete the project
* Provide a record of any issues or risks that you faced creating your project
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture described fully in the next section
* The project must be deployed using containerisation and an orchestration tool
* As part of the project, it will need to create an Ansible Playbook that will provision the environment that the application needs to run
* The project must make use of a reverse proxy to make the application accessible to the user

## Architecture

Expanding on the brief the project must follow a strict architetcture which consists of four services that operate in conjunction with eachother to produce an output for the user. 

### Service one 

The core service – this will render the Jinja2 templates needed to interact with the application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

### Services two and three

Services two and three will create outputs that appear random to the user.

### Service four

This service will process the output from services two and three and will produce different results depending on the ouput it has recieved.

## My Application

* My application will be a rap name generator based on the popular online wu-tang name generator
* Service one will act as you'd expect displaying a page for user input and their result from the generator
* Service two will take the first name input and return a letter and service three will take the second name input and then return a number
* Service four will take the resulting letter and number and return a rap name determined by the letter and number it receives

At first I created a design for the app that would pass user input from service 1 to services 2 and 3 seperately then thos would pass their output to service 4 which would then return an output to service 1. You can see the model of the application flow below.

![App flow original](https://user-images.githubusercontent.com/56595709/86147421-496d3580-baf1-11ea-90a3-53ba11058101.jpg)

Although the original design may have worked I believe it would be much more difficult to implement than the final design, instead of having all the apps making post requests to and from each other it make more sense to have service 1 making all the requests as a central hub for the application and the other services just returning the result of their function. The final design for the applications services flow can be seen in the diagram below. 

![App Flow](https://user-images.githubusercontent.com/56595709/86761086-a0b55d80-c03d-11ea-831c-5a14d17fa2f3.jpg)

## CI Pipeline

Once the application design was in place it was time to start thinking about what the CI Pipeline would look like. It was important to have a cler understanding of not only how the application would work but also map out the automation of testing and deployment. Below is a diagram of the CI Pipeline for all the processes involved in creating and automating the application.

![CI Pipeline](https://user-images.githubusercontent.com/56595709/87245716-8d403300-c43f-11ea-911b-64dc6b37b76a.jpg)

To expand on what you can see in the diagram have source code of the application itself, when I changed is implemented i.e. pushing to github it triggers a jenkins pipeline build using a jenkinsfile. This jenkins build follows the flow you can see in the devops section of the diagram and will use the jenkinsfile to run a script that builds the containers according to the code pulled from github and pushes the images up to dockerhub where they can be used by docker swarm for deployment of the lastest version of the application. Once the containers are built and pushed the testing will run and print coverage reports in the console for analysis.

Once the tests are complete the Jenkinsfile moves on to the configuration and deployment stage the deployment and configuration script runs an ansible playbook which will install docker and docker compose on the all host machines. Once docker and docker-compose are installed then the playbook will initialise a swarm on the manager machine and join that swarm as a worker on another machine. Once the swarm has been created the playbook will then deploy the stack on the swarm it has created and the app is then available from each machine.

Below is an image outlining the ansible plays for configuration and deployment and the machines on which they occur.

![Ansible plays diagram](https://user-images.githubusercontent.com/56595709/87246336-b616f700-c444-11ea-9476-58a69b98d9d4.jpg)
