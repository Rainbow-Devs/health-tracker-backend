# base image
FROM python:3.11-alpine

# set work directory
RUN mkdir -p /app

# where your code lives
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . .
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs
EXPOSE 8000
# start server
ENTRYPOINT ["/app/entrypoint.sh"]
