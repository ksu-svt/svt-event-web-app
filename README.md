# svt-event-web-app
A web application that keeps track of SVT events and member activities.

## Getting Started
This is quick introduction on how to get the code on your machine and run the server from the command line.

### Clone the Repo
First, clone the repo onto your local machine.
```shell
git clone https://github.com/ksu-svt/svt-event-web-app.git
```

### Setup the Project
The first step that must be done is to setup the models, so we can provision a new database for development. To do this we can use the `migrate` command for the `manage.py` script. Run the following command from **inside** the `svt-event-web-app/` directory:
```shell
python manage.py migrate
```

### Create Superuser
In order to access the Django admin panel, you need to create a new superuser for the web application. You can do this by using the `createsuperuser` command.

```shell
python manage.py createsuperuser
```

### Launching the Web Application
Finally, we can launch the web app. Simply, run the command:
```shell
python manage.py runserver
```
**Note:** If you are running PyCharm, you should be able to setup a Run Configuration to automatically run the web application.
