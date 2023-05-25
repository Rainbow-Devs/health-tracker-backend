Welcome! This will eventually be the backend for the Rainbow Devs
[health-tracker frontend](https://github.com/Rainbow-Devs/health-tracker).

The following steps will share how to get your development machine set up to
run the backend and start contributing to the repository.

# Prepare your computer

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

# Running the Django server

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

When you're all done, you can use [CTRL] + [C] in your terminal to quit the
Django server. Then, to exit out of the virtual environment, run this command:

```bash
deactivate
```

# Where to go from here

If you'd like more information about Django, follow the getting started
tutorial provided by the official project documentation:

[https://docs.djangoproject.com/en/4.2/intro/tutorial01/](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

For more about Graphene and using it in Django, you can find its
documentation here:

[https://docs.graphene-python.org/projects/django/en/latest/](https://docs.graphene-python.org/projects/django/en/latest/)
