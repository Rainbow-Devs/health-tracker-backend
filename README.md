# Health Tracker Backend

This is the backend webapp for the Rainbow Devs Health Tracker application. For
the frontend app, that can be found at
[Rainbow-Devs/health-tracker-frontend](https://github.com/Rainbow-Devs/health-tracker-frontend).

The following steps will share how to get your development machine set up to
run the backend and start contributing to the repository.

## Prepare your computer

To prep your computer for Python + Django development, create a virtual Python
environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

Next, install the required `pip` packages for the project:

```bash
pip install -r requirements.txt
```

Then, set a secret key:

```bash
cp .env.example .env
```

Edit your `.env` file to add a randomly-generated string to the `SECRET_KEY`
environment variable.

## Running the Django server

Now that you have the required packages installed, let's run the available
database migrations:

```bash
python manage.py migrate
```

Then, let's go ahead and start the Django server:

```bash
python manage.py runserver
```

You can verify the server is working and the Graphene (GraphQL) package is
being served up by visiting [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql).

## Stopping the Django server

When you're all done, you can use `CTRL` + `C` in your terminal to quit the
Django server. Then, to exit out of the virtual environment, run this command:

```bash
deactivate
```

## Linting and formatting

To lint your Python code, you can run the following (after activating your
`venv` virtual environment):

```bash
prospector healthtracker
```

This should both lint your code (using `pylint`) as well as check your code
formatting.

## Post-deployment checks

```bash
python manage.py check --deploy
```

## Running with Docker

There are two ways to create and run the Docker container image: building and
running manually with Docker or by creating a `docker-compose.yml` file and
using Docker Compose to start the webapp.

### Docker Compose

For Docker Compose, this is a minimal configuration that will get you started:

```yaml
services:
  health-tracker-backend:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: health-tracker-backend
    image: rainbow-devs/ht-backend
    ports:
      - "8000:8000"
```

From there, you can follow these steps to build and run the container image:

```bash
docker compose build --pull
docker compose up -d
```

Finally, when you're done, use this command to stop the container and remove the
container image:

```bash
docker compose down
```

## Where to go from here

If you'd like more information about Django, follow the getting started
tutorial provided by the official project documentation:

[https://docs.djangoproject.com/en/4.2/intro/tutorial01/](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

For more about Graphene and using it in Django, you can find its
documentation here:

[https://docs.graphene-python.org/projects/django/en/latest/](https://docs.graphene-python.org/projects/django/en/latest/)
