# dj-apis-allauth
Django Rest Framework  API Endpoints secure Authentications . This package is ideal for Mobile Applications or Single Page Application Integration such  as Flutter, VueJs, React, AngularJs etc....

[![Published on Django Packages](https://img.shields.io/badge/Published%20on-Django%20Packages-0c3c26)](https://djangopackages.org/packages/p/dj-apis-allauth/)

# Why this project ?

The maintainer of "dj-rest-auth" is no longer interested in maintaining the project with Django-allauth issues and nor accepting pull requests.
So I have started this project to help the Good cause of Open Source Software greatness lives on.
So anybody that uses this package and willing to help maintain it is more than welcom to fork it and make a pull request.
Thanks.

# The regular django api token with user's info


<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-56-57" src="https://github.com/user-attachments/assets/0009a3a8-b28b-4585-bc57-e12568e6ded4" />

This is the token and user info

<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-57-16" src="https://github.com/user-attachments/assets/dd410bea-1c83-4e68-a2db-7f92115f296f" />


# This is the JWT token return endpoint

<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-57-57" src="https://github.com/user-attachments/assets/4c097266-404c-4659-bed3-23f5ff84c0fc" />

<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-58-19" src="https://github.com/user-attachments/assets/b3bc8051-6969-4678-a8d7-a69a82a53bdd" />



#  A simple registration page

<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-53-51" src="https://github.com/user-attachments/assets/9405278c-b98e-47a5-b261-26d86e5805e5" />


## Requirements
- Django >= 4.2
- Python >= 3.12

## Quick Setup

Install package

    pip install dj-apis-allauth
    
Add `dj_api_auth` app to INSTALLED_APPS in your django settings.py:

```python
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_apis_allauth'
)
```
    
Add URL patterns

```python
urlpatterns = [
    path('dj_apis_allauth/', include("dj_apis_allauth.urls")),
]
```
    

(Optional) Use Http-Only cookies

```python
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}
```

### Testing

Install required modules with `pip install -r  dj_apis_allauth/tests/requirements.txt`

To run the tests within a virtualenv, run `python runtests.py` from the repository directory.
The easiest way to run test coverage is with [`coverage`](https://pypi.org/project/coverage/),
which runs the tests against all supported Django installs. To run the test coverage 
within a virtualenv, run `coverage run ./runtests.py` from the repository directory then run `coverage report`.

#### Tox

Testing may also be done using [`tox`](https://pypi.org/project/tox/), which
will run the tests against all supported combinations of Python and Django.

Install tox, either globally or within a virtualenv, and then simply run `tox`
from the repository directory. As there are many combinations, you may run them
in [`parallel`](https://tox.readthedocs.io/en/latest/config.html#cmdoption-tox-p)
using `tox --parallel`.

The `tox.ini` includes an environment for testing code [`coverage`](https://pypi.org/project/coverage/)
and you can run it and view this report with `tox -e coverage`.

Linting may also be performed via [`flake8`](https://pypi.org/project/flake8/)
by running `tox -e flake8`.

### Documentation

Work in progress...
https://dj-apis-allauth.readthedocs.io/en/latest/


### Acknowledgements

This project began as a fork of `django-rest-auth` and "dj-rest-auth" . Big thanks to everyone who contributed to that repo!

#### A note from Me
I will be trying my best to maintain this project but anyone is welcom to help maintain it.
There is so many features that I am planning on adding to this.
So feel free to make propositions on features that should be added.
Thanks.
