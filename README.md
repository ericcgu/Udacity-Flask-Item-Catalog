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

Python Flask SQLAlchemy Starter with Google oAuth 2.0

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
Functionality is isolated and de-coupled for single responsiblity as much as possible. 
Package modules to promote code re-use and collaboration.

```bash
.
├── Dockerfile                  #Dockerfile is optimized for pip caching.
├── config                      
│   └── settings.py             #Considered YAML, environment classes inherit from Default class.
├── docker-compose.yml
├── app
│   ├── egu-nyc-dev-001.db      #Required db objects are seeded with Faker library.
│   ├── forms
│   │   └── item.py             #Create/Update share common form.
│   ├── models
│   │   ├── category.py         #Used hybrid property and hybrid expression to dynamically calc child relationships.
│   │   ├── item.py
│   │   └── user.py
│   ├── routes
│   │   ├── category.py
│   │   ├── errorhandlers.py
│   │   ├── item.py
│   │   ├── main.py
│   │   └── userauth.py
│   ├── services
│   ├── static
│   │   ├── img
│   │   │   └── google.png
│   │   └── styles
│   │       └── main.css
│   └── templates
│       ├── errors
│       │   ├── 403.html
│       │   ├── 404.html
│       │   └── 500.html
│       ├── item.html
│       ├── layout.html
│       └── main.html
├── manage.py
└── requirements.txt
```

* `Docker`  - Dockerfile is optimized for pip caching. Other services can be orchestrated via Docker-Compose
* `authors` - Contains list of authors who have published their articles.
* `log` - Stores log of every request sent to the newspaper server.

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


## Installation

### Requirements

Docker (https://www.docker.com/get-started)

### Deploy

```bash
#clone repo
cd src/web
docker-compose up --build
```

### Teardown

```bash
docker-compose down
```

[(Back to top)](#top)
