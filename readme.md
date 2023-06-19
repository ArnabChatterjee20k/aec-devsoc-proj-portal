# About
The backend for our Dev Soc Project portal

# Objectives
*  Students,Professors,Alumi can create project and submit to get the team members or contributors

*  They can contribute to a project

*  Their Profile reflect on what they have taken

# Contributing
### wrting tests
* you write all the tests in the file starting with prefix test_ (preferably test_app) in forms of function of format test_functionn_name


* running tests

```bash
    pytest
```

* before making prs make sure the tests are written for your code

# Local Setup
* if using docker then connect to mongo database by
  ```bash
  docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server:6.0-ubi8
  ```

# Documentation
go to /docs endpoint of the api
