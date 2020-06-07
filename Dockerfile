FROM python:3.7.7-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install gcc libpq-dev
COPY requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/prod.txt && rm -rf /tmp/requirements
RUN mkdir /opt/dugong
COPY . /opt/dugong
WORKDIR /opt/dugong
RUN touch .env

EXPOSE 8000

# CMD  ["/usr/bin/supervisord"]
