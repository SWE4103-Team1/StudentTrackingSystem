# TestMerge
It is a repo for testing.
This is the dev branch, and only your name-feature can be merged into this.

## Dependencies

1. Install system packages, listed below

    **mysqlclient**

    MySQL client must be separately installed as a system package.

    The *mysqlclient* Python package contains Python bindings to the MySQL client.
    Django depends upon this package, such that it can access MySQL. However, this
    package does not ship the actual MySQL client, merely the Python bindings to it.
    As such, the MySQL client must be separately installed as a system package.
    Installation information can be found at the [pypi package
    listing](https://pypi.org/project/mysqlclient/). On arch-linux, it was as simple as:
    `yay -S mysql`.

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


## Database Connection

The database is currently publically accessible, but has a subnet group with source IP address restrictions to it. If you would like direct connection to the database, contact Justen.
