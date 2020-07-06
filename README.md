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

![App Flow](https://user-images.githubusercontent.com/56595709/86147421-496d3580-baf1-11ea-90a3-53ba11058101.jpg)

* My application will be a rap name generator based on the popular online wu-tang name generator
* Service one will act as you'd expect displaying a page for user input and their result from the generator
* Service two will take the first name input and return a letter and service three will take the second name input and then return a number.
* Service four will take the resulting letter and number and return a rap name determined by the letter and number it receives.
