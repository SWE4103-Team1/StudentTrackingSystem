# Student Tracking System

[![Django CI](https://github.com/SWE4103-Team1/StudentTrackingSystem/actions/workflows/django.yml/badge.svg?branch=dev)](https://github.com/SWE4103-Team1/StudentTrackingSystem/actions/workflows/django.yml)
***
## ***Visit our website on [Student Tracking System](http://swe4103production-env.eba-tq53gcxr.us-east-1.elasticbeanstalk.com)***
***
## Dependencies

1. Install system packages, listed below

   **mysqlclient**

   MySQL client must be separately installed as a system package.

   The _mysqlclient_ Python package contains Python bindings to the MySQL client.
   Django depends upon this package, such that it can access MySQL. However, this
   package does not ship the actual MySQL client, merely the Python bindings to it.
   As such, the MySQL client must be separately installed as a system package.
   Installation information can be found at the [pypi package
   listing](https://pypi.org/project/mysqlclient/).

   On arch-linux, run `yay -S mysql`. With debian/Ubuntu, `sudo apt install libmysqlclient-dev` will work.

2. First, ensure you create and activate a Python virtual environment in this
   project's root:

   ```bash
   python -m venv venv        # create
   source ./venv/bin/activate # activate
   ```

   activate scripts exist for various shells

3. All _pip_ dependencies are listed in the `requirements.txt` file, and can be
   installed with:

   ```bash
   pip install -r requirements.txt
   ```

## Database Connection

There are 2 database options: SQLite and MySQL. MySQL connects to the hosted, "real" database in AWS. SQLite makes a local file and uses that as the datastore for a local database instance.

### MySQL

The database is currently publically accessible, but has a subnet group with source IP address restrictions to it. If you would like direct connection to the database, contact Justen.

### SQLite

The current CI configuration uses the SQLite database.
SQLite can be used by setting the environment variable USE_SQLITE to TRUE, and then starting the Django tests or server, as usual.

If you're unfamiliar with environment variables, an exported evironment variable in a shell session will persist for the extent of the shell session, but on a different shell session, you will have to export the variable, again.

Environment variable examples on MacOS & Linux:

```bash
export USE_SQLITE=TRUE  # set to TRUE (use SQLite)
export USE_SQLITE=FALSE # set to FALSE (disable SQLite)
unset USE_SQLITE        # unset (disable SQLite & remove var)
```

If this is the first invocation using the SQLite database, you first need to create the database schema. Do this with the following Django command, from the same directory as _manage.py_:

```bash
python manage.py migrate
```

## Data & Config Files

A user is to upload many files to the program, both to configure the operation of the program, and to upload actual data. Sample data and config files are included in the `data/` folder, which can be used for testing.

**Data Files:**

- studentData.txt
- courseData.txt
- transferData.txt

**Configuration Files:**

- rank-prerequisites.xlsx
- SWEProgram.xlsx

The configuration files must be uploaded prior to the data files. However, when
testing the program with `python manage.py test ...` the local config files will
automatically loaded. Additionally, setting the environment variable
`USE_LOCAL_CONFIGS=TRUE` will also cause the program to pre-load these config
files. This is useful when locally testing with `python manage.py runserver ...`. Check `manage.py` for details.

## CI

Now our repo has successfully deployed Django CI through Github Action!

- This will automatically run Django Test when you push or merge and return a result to tell you whether your project successfully ran this test.
- If you get a failed result, click the **Action** button to view the log.
- This branch is merged from the **dev** branch because this is the latest branch after sprint1.
- Branches that start with dev\_ will automatically run CI when pushed to GitHub

## Git Standards

### fetch, push & merge

For coding, please

- choose one dev branch from the lists
- create one new branch, like feature_Tom
- checkout to your branch and code
- commit and push to your branch
- merge your branch into the latest dev branch and delete your feature branch

### differnences between dev and feature

- **choose feature_xxxx** just for checkouting from dev\_**_ and _**delete\*\*\* it after merging
- **choose dev_xxxx** for merging your code with others and **delete your feature** branch after that. delete old dev if you all are working on new dev

### main

After completing all development of a phase

- merge all dev branches into the main branch
- update the version number, like STS 1.0
- delete all feature branches
- write a document for this version
