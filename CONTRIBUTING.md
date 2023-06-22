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
pip install -r requirements/prod.txt
```

Prepare the App

```
python src/manage.py makemigrations --settings="config.settings.local"
python src/manage.py migrate --settings="config.settings.local"
```

Run
---

Start the server

```
python src/manage.py runserver --settings="config.settings.local"
```

