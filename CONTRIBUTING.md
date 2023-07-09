Contributing
============

Setup
-----

Clone repository and submodule

```
git clone git@github.com:dragonleman/django-example.git
```

Create and activate a virtual env (with [pyenv](https://github.com/pyenv/pyenv))

```
pyenv install 3.8.7
pyenv virtualenv 3.8.7 django-example
pyenv activate django-example
```

Install dependencies

```
pip install -r requirements/local.txt
```

Prepare the App

```
python src/manage.py makemigrations
python src/manage.py migrate
```

Run
---

Start the server

```
python src/manage.py runserver
```

