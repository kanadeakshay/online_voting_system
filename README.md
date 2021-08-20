# Online Voting System

## Table of Contents

- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Local Setup](#local-setup)
- [Licence](#licence📃)
<!-- - [Screenshots](#screenshots🖼) -->

## Introduction

I try to build a website where **online elections** can be conducted. I build this site using django framework.

## Motivation

This is a side project I build to test my Django skills.

## Features

- Only authenticated voters/citizens can register in the system and vote.
- Voters can vote only one time.
- Only one election can be conducted at a time by Admin.
- Admins and voters of that particular region can see history of all elections conducted and their winners.
- There is Message on voters dashboard of the current state of election.

<!-- ## Screenshots🖼 -->

## Tech stack

- Frontend :
  - HTML
  - CSS
  - JavaScript
- Backend :
  - Django

## Local Setup

### 1. First clone this repo or you can also fork it and then clone it

```bash
git clone https://github.com/akshay782/online_voting_system.git
```

### 2. Go to project directory and run this two commands

```python
python manage.py migrate
python manage.py makemigrations
```

Now before running this project into browser we have to set some **Regions** and **Admins** for that regions. For that we have to create superuser so that we access **Django Admin Dashboard**.

### 3. Creating superuser

Run the following command -

```bash
python manage.py createsuperuser
```

Set a username and password \
Now, go to `http://127.0.0.1:8000/admin` and fill the login form \
First open Regions model and set some regions and second open Admins model and set admins for that regions.\
Now we are all set for running the project 👍

At this point you can access only admin side of project like login as an admin(we set in **Admins** models), creating elections etc.

Go to `http://127.0.0.1:8000/` on your browser and you can login as a admin

### 4. Setting dummy data of voters

For login as voter I already set some citizens data on citizens_data folder. You can login as those but I will suggest to add your own citizens with dummy info and their regions same as you set in **Regions** model. Now we can register and login as voter that we created in citizens.csv file.\
Finally all setup is completed 😊

### 5. Running project into browser

Run the following command -

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/`

### 6. This is only for if you fork the repo and want to commit the changes into your forked repo.

```bash
git add .
git commit -m "message"
git push origin <branch-name>
```

## Licence📃

- [MIT License](/LICENSE)
