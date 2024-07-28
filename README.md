django-autoresponse-middleware
======
Django middleware to reduce the boilerplate of HttpResponse construction.  If views return strings or dicts, HttpResponse and JsonResponse objects will be automatically constructed.  Status codes and headers can also be returned.

### Install
```pip install django-autoresponse-middleware```


### Usage
```python

MIDDLEWARE = [
    ...,
    'django_autoresponse_middleware.middleware',  # must be last
]
```


#### Simplified Django views
```python

def index(request):
    return "hello world!"


def unauthorized(request):
    return "unauthorized", 400


def ping(request):
    return {"message": "pong"}, 200, {"MY-RESPONSE-HEADER": "abc"}
```

----
[![Coverage Status](https://coveralls.io/repos/github/dpep/django-autoresponse-middleware/badge.svg?branch=main)](https://coveralls.io/github/dpep/django-autoresponse-middleware?branch=main)
[![installs](https://img.shields.io/pypi/dm/django-autoresponse-middleware?label=installs)](https://pypi.org/project/django-autoresponse-middleware)
