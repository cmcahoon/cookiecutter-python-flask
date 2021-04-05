# {{cookiecutter.directory_name}}

> This project was generated using `cookiecutter`.


## Overview

This repository is a Python 3.9 REST service using the following libraries:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - REST Framework
- [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database ORM
- [Alembic](https://flask-migrate.readthedocs.io/en/latest/#) - Database Migrations
- [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - Input Validation
- [Requests](https://requests.readthedocs.io/en/master/) - REST Client


## Structure
```
project-root
|   README.md
|---{{cookiecutter.module_name}}
|---migrations
```

| File/Directory | Description |
| --- | --- |
| `README.md` | This file! |
| `{{cookiecutter.module_name}}/` | Root Python module. |
| `migrations/` | Alembic migration directory. |


## Getting Started

This section is to go from repository creation to running application quickly. The specifics of local development are in a subsequent section.


### Run with Docker Compose

The entire stack required for this application is declared in `docker-compose.yml`. There are three services:
- `init` - Ensures the database is migrated to the latest schema. It will quit when done, which is normal.
- `rest` - Flask application
- `postgres` - Application database.

From the project root:
```bash
docker-compose up --build
```

Once up and running you can use Postman or cURL to send requests to endpoints at `http://localhost:5000`.


## Local Development

You will likely want to use this bootstrapped project as a spring board for developing a new Flask service. These directions will talk about customizing it to fit your needs.


### Create a virtual environment using `pipenv`

First, you will need to install [Pipenv](https://docs.pipenv.org/).

Once installed, run the following commands from the project root:
```bash
# Install the dependencies
pipenv install

# [OPTIONAL] If Pipenv complains about your Python version (e.g., it cannot find Python 3.9), you can provide the path explicitly
pipenv install --python /path/to/python3

# Install the development dependencies (linter, formatter, typing)
pipenv install -d
```


### Define models and validation schemas

You most likely don't need a `User` model, or need to define other database modules. These are the foundation for Alembic's migrations and Marshmallow's validation schemas.

In `{{cookiecutter.module_name}}/model.py` define SQLAlchemy models that meet your needs.

Once defined, add schemas in `{{cookiecutter.module_name}}/validation.py`. As an example:
```python
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User  # Set this to the model you want to use as the basis for validation schema

    @post_load
    def make_model(self, data, **kwargs):
        return User(**data)
```

The `@post_load` annotation will convert a dict to the model defined in the `Meta` inner class. This is useful when you want to perform input validation on a request body and then use the model to interact with the database.


### Create a database migration

> You probably don't want the migration for the `User` table so the directions will have you remove the existing, example migrations directory.


From the project root:
```bash
# Remove the migrations directory
rm -rf migrations

# Initialize Alembic -- this will recreate a fresh migrations directory
FLASK_APP={{cookiecutter.module_name}} python -m flask db init

# Create your first migration
FLASK_APP={{cookiecutter.module_name}} python -m flask db migrate -m "Initial migration."
```

You will now have a migration in the `migrations/versions/` directory. Alembic's documentation states you should look over the migrations carefully -- they sometimes fail to capture all model changes.


### Migrate the database

If using Docker Compose, just `docker-compose down` to clean up. When you run `docker-compose up` the next time it will initialize the database with your new schema.

If you want to do it manually make sure that the `DATABASE_URI` environment variable is set or provided in the `.env` file. Then, from the project root:
```bash
FLASK_APP={{cookiecutter.module_name}} python -m flask db upgrade
```

