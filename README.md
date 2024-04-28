<h1 align="center">
    <picture>
        <img width="343" src="screenshots/django-blogs.svg" alt="django-blogs">
    </picture>
</h1>
<p align="center">
    <br>
    <a href="https://github.com/gh0stfrk/djangoblogs/actions">
        <img src="https://github.com/gh0stfrk/djangoblogs/workflows/Django%20CI/badge.svg" alt="Build Status" />
    </a>
    <a href="https://opensource.org/licenses/BSD-3-Clause">
        <img src="https://img.shields.io/badge/license-BSD-blue.svg" alt="License" />
    </a>
    <a href="https://twitter.com/gh0stfrk">
        <img src="https://img.shields.io/twitter/follow/gh0stfrk?style=social&logo=twitter" alt="follow on Twitter">
    </a>
</p>
Django Blogs is a simple and lightweight blogging application built with Django.

It allows users to register and create blogs where they can write short and informative posts.

## 🔥 Features
- Sign up and create profiles, customize your profiles with avatars
- Create mini-blog posts, update them and share them
- Likes and Comments, like posts and comment with your thoughts.

## 📦 Structure 
- Django project contains two applications one is `users` and the other one is `blogs`.
`users` app controls all things user-related, including signing up, registering and updating user information.
- Signals are used to create a user profile when a user is created, the user profile contains additional information about the user, such as a profile photo.
- `blogs` app is responsible for creating and updating blogs.

## 🏛️ Infrastructure
![deployment](./screenshots/deployment_dig.png)

## 👷 Development Environment 
- Clone the latest branch
```bash
git clone https://github.com/gh0stfrk/django-blog.git
cd djangoblog
```
- Create a virtual environment (use python 3.10)
```
python3 -m venv venv
source ./venv/source/activate
```
- Install dependencies Setup Postgres database credentials in a .env file, copy the contents of [.sample.env](./sample.env)
```bash
pip install -r requirements-deploy.txt
```

