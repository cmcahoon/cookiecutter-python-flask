# STAGE - builder
FROM python:3.9 as builder
WORKDIR /src
RUN apt-get update &&\
    apt-get install -y build-essential
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy


# STAGE - lightweight runtime
FROM python:3.9
WORKDIR /opt/smarter-sorting/{{cookiecutter.directory_name}}
RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh &&\
    chmod +x wait-for-it.sh

COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=builder /usr/local/bin/ddtrace-run /usr/local/bin/ddtrace-run
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY {{cookiecutter.module_name}} {{cookiecutter.module_name}}
COPY migrations migrations

ENV PYTHONPATH "${PYTHONPATH}:/opt/smarter-sorting/{{cookiecutter.directory_name}}"

CMD ["gunicorn", "-b", "0.0.0.0:5000", "{{cookiecutter.module_name}}:create_app()"]