[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo svg">
</a> 

# Job Market

## Table of Contents <!-- omit in toc -->

- [Motivation](##Motivation)
- [Design & Architecture](#Design-and-Architecture)
- [Concepts](#Concepts)
- [Docker](##Docker)
- [Installation](#Installation)

## Synopsis

Full Stack Python Flask SQLAlchemy Starter with Google oAuth 2.0

![screen shot 2018-10-11 at 12 44 56 am](https://user-images.githubusercontent.com/4943759/46781311-f89b2500-ccee-11e8-8cca-7db4ab5ba128.png)

![screen shot 2018-10-11 at 12 54 56 am](https://user-images.githubusercontent.com/4943759/46781655-ae1aa800-ccf0-11e8-9215-633493a16738.png)

## Design and Architecture

This application is organized around a MVC pattern. 

```bash
.
├── config
└── app
    ├── models      # Model
    ├── routes      # Controller
    ├── templates   # View
    ├── forms
    └── static
```
Modules/Features are isolated and de-coupled for single responsiblity. 

Organized into Package modules to promote code readability, re-use and collaboration.

```bash
.
├── Dockerfile                # Dockerfile is optimized for pip-install Container caching.
├── config                      
│   └── settings.py           # Considered YAML, environment classes inherit from Default class.
├── docker-compose.yml
├── app
│   ├── egu-nyc-dev-001.db    # Required db objects are seeded with Faker library.
│   ├── forms
│   │   └── item.py           # Create/Update re-leverage/share unified form.
│   ├── models
│   │   ├── category.py       # Hybrid property/expression to dynamically calc child relationships.
│   │   ├── item.py
│   │   └── user.py
│   ├── routes
│   │   ├── category.py
│   │   ├── errorhandlers.py
│   │   ├── item.py
│   │   ├── main.py           # Leveraged marshmallow for serialization. Single endpoint with nested children.
│   │   └── userauth.py       # Receives a signal/instance of blueprint and token via Flask-Dance.
│   ├── services
│   ├── static
│   │   ├── img
│   │   │   └── google.png
│   │   └── styles
│   │       └── main.css
│   └── templates             # Limited and avoided logic in templates. Used Bootstrap and modal window.
│       ├── errors
│       │   ├── 403.html      # Custom error handlers
│       │   ├── 404.html
│       │   └── 500.html
│       ├── item.html
│       ├── layout.html
│       └── main.html
├── manage.py
└── requirements.txt
```

``` python

    @hybrid_property
    def item_count(self):
        return len(self.items)

    @item_count.expression
    def item_count(cls):
        return (select([func.count(Item.id)])
                .where(Item.category_id == cls.id)
                .label("item_count"))
```
## Docker

## API

```bash
http://localhost:8000/
```

## Installation

### Requirements

Docker (https://www.docker.com/get-started)

### Deploy

```bash
# Clone this repository using git
cd src/web
docker-compose up --build
# Navigate to http://localhost:8000/
```

### Teardown

```bash
docker-compose down
```

[(Back to top)](#top)
