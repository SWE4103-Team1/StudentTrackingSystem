[![Django CI](https://github.com/SWE4103-Team1/StudentTrackingSystem/actions/workflows/django.yml/badge.svg?branch=dev)](https://github.com/SWE4103-Team1/StudentTrackingSystem/actions/workflows/django.yml)
[![Build Status](http://3.86.91.241:8080/buildStatus/icon?job=git_test)](http://3.86.91.241:8080/job/git_test/)

# Student Tracking System

## Dependencies

1. Install system packages, listed below

    **mysqlclient**

    MySQL client must be separately installed as a system package.

    The *mysqlclient* Python package contains Python bindings to the MySQL client.
    Django depends upon this package, such that it can access MySQL. However, this
    package does not ship the actual MySQL client, merely the Python bindings to it.
    As such, the MySQL client must be separately installed as a system package.
    Installation information can be found at the [pypi package
    listing](https://pypi.org/project/mysqlclient/).

    On arch-linux, run `yay -S mysql`. With debian/Ubuntu, `sudo apt install
    libmysqlclient-dev` will work.

2. First, ensure you create and activate a Python virtual environment in this
    project's root:

    ```bash
    python -m venv venv        # create
    source ./venv/bin/activate # activate
    ```

    activate scripts exist for various shells

3. All *pip* dependencies are listed in the `requirements.txt` file, and can be
    installed with:

    ```bash
    pip install -r requirements.txt
    ```

## Database Connection

The database is currently publically accessible, but has a subnet group with source IP address restrictions to it. If you would like direct connection to the database, contact Justen.

## 10.19-update

Now our repo has successfully deployed Django CI through Github Action!
- This will automatically run Django Test when you push or merge and return a result to tell you whether your project successfully ran this test.
- If you get a failed result, click the **Action** button to view the log.
- This branch is merged from the **dev** branch because this is the latest branch after sprint1.
********

## fetch, push & merge

For coding, please
- choose one dev branch from the lists
- create one new branch, like feature_Tom
- checkout to your branch and code
- commit and push to your branch
- merge your branch into the latest dev branch and delete your feature branch
******

## differnences between dev and feature

- **choose feature_xxxx** just for checkouting from dev_*** and ***delete*** it after merging
- **choose dev_xxxx** for merging your code with others and **delete your feature** branch after that
- delete old dev if you all are working on new dev
*******

## main

After completing all development of a phase
- merge all dev branches into the main branch
- update the version number, like STS 1.0
- delete all feature branches
- write a document for this version


