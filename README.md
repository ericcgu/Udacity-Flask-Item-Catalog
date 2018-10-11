[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo svg">
</a> 

# Job Market

## Table of Contents <!-- omit in toc -->

- [Motivation](##Motivation)
- [Design & Architecture](#Design-and-Architecture)
- [Concepts](#Concepts)
- [Installation](#Installation)

## Motivation

Python Flask Starter with oAuth 2.0

## Design and Architecture

This application is organized around an MVC pattern. 

.
├── config
└── app
    ├── models      <----model
    ├── routes      <----controller
    ├── templates   <----view
    ├── forms
    └── static

## Concepts

.
├── Dockerfile
├── config
│   └── settings.py
├── docker-compose.yml
├── app
│   ├── egu-nyc-dev-001.db
│   ├── forms
│   │   └── item.py
│   ├── models
│   │   ├── category.py
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
