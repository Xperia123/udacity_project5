# Capstone Project (Cloud DevOps Engineer)

Capstone project for Udacity Dev-Ops Nanodegree: develop a CI/CD pipeline for micro services applications with either blue/green deployment or rolling deployment.

## CI CD Pipeline

The CI CD pipeline is as follows for this project. For initial set up:

- Set up CircleCI
- Install dependencies for local development
- Create AWS infrastructure

For application development:

- Make development change
- setup CircleCI
- Commit to git
- Push to repository

## Running the stuff

There is a `Makefile` that contains lots of useful commands.
Running `make` will list them, like the below output.

```text
setup:          Create the virtial environment to run this project
install:        Install the required imports for this project
test:           Run the tests for this prject
lint:           Check the validity of the project files
```


## CircleCI setup

Link CircleCI to project github
Add Enviroment on CircleCI 

## Output

From running the above the following will be created.

CIRCLECI FLOW:
![Full pipline pass](./Image/Pipeline success.PNG)

CircleCI build when the lint fails:
![lint failing](./Image/Check code false.PNG)

CircleCI build when the lint pass:
![lint pass](./Image/Check code pass.PNG)

Build stack on Cloudformation:
![Screenshot-cloudformation-create](./Image/CloudFormation create.PNG.png)

Create EC2 Success:
![Screenshot-ec2-runing](./Image/EC2 Running.PNG)

Create EKS Success:
![Application running in AWS](./Image/Eks.PNG)

Output:
![Screenshot-output](./Image/output.PNG)