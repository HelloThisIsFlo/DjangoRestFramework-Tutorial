
# Django Rest Framework - Tutorial

From: https://www.django-rest-framework.org/tutorial/1-serialization/

## Notes
### Authentication
For register/login/logout, the official documentation recommends using the provided views from `django.contrib.auth`. But for a Single-Page App, this isn't working.

For a register/login/logout flow fully integrated via a REST interface, check: [`django-rest-auth`](https://github.com/Tivix/django-rest-auth) (recommended [here](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-auth))
