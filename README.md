# dj-apis-allauth
Django Rest Framework  API Endpoints secure Authentications . This package is ideal for Mobile Applications or Single Page Application Integration such  as Flutter, VueJs, React, AngularJs etc....

[![Published on Django Packages](https://img.shields.io/badge/Published%20on-Django%20Packages-0c3c26)](https://djangopackages.org/packages/p/dj-apis-allauth/)

# Why this project ?

The maintainer of "dj-rest-auth" is no longer interested in maintaining the project with Django-allauth issues and nor accepting pull requests.
So I have started this project to help the Good cause of Open Source Software greatness lives on.
So anybody that uses this package and willing to help maintain it is more than welcom to fork it and make a pull request.
Thanks.

# The regular django api token with user's info

<img width="1535" height="958" alt="Screenshot from 2025-09-24 01-33-56" src="https://github.com/user-attachments/assets/3836823e-99af-4444-9cd2-7a29c6e6519d" />

This is the token and user info

<img width="1535" height="958" alt="Screenshot from 2025-09-24 01-44-22" src="https://github.com/user-attachments/assets/9e58c546-5e29-4a21-a195-2a5030de3d65" />

# This is the JWT token return endpoint

<img width="1535" height="958" alt="Screenshot from 2025-09-24 01-51-16" src="https://github.com/user-attachments/assets/cc843beb-c8c7-4cda-9f00-cc73dbe6e19c" />


<img width="1535" height="958" alt="Screenshot from 2025-09-24 01-51-29" src="https://github.com/user-attachments/assets/42746d44-4a31-4661-be37-053eb966ab27" />




#  A simple registration page


<img width="1282" height="951" alt="Screenshot from 2025-09-24 18-44-55" src="https://github.com/user-attachments/assets/1f7852d1-4aae-4ce4-9bb0-1e2322ef78b3" />




## Requirements<img width="1328" height="981" alt="Screenshot from 2025-09-26 18-53-51" src="https://github.com/user-attachments/assets/9405278c-b98e-47a5-b261-26d86e5805e5" />

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


### Acknowledgements

This project began as a fork of `django-rest-auth` and "dj-rest-auth" . Big thanks to everyone who contributed to that repo!

#### A note from Me
I will be trying my best to maintain this project but anyone is welcom to help maintined it.
There is so many features that I am planning on adding to this.
So feel free to make propositions on features that should be added.
Thanks.
