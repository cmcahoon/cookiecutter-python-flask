# cookiecutter-python-flask


## Overview

This repository is a Python 3.9 REST service using the following libraries:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - REST Framework
- [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database ORM
- [Alembic](https://flask-migrate.readthedocs.io/en/latest/#) - Database Migrations
- [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - Input Validation
- [Requests](https://requests.readthedocs.io/en/master/) - REST Client


## Prerequisites

All you need to use this template is [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html).


## Usage

```bash
$ cookiecutter https://github.com/cmcahoon/cookiecutter-python-flask
directory_name [my-service]: api-cookie
module_name [my-module]: cookie
database_name [my-database]: cookie_jar
```

Once complete the `api-cookie` directory will have a Flask application ready to go! The README provides instructions to get started with Docker Compose and local development.