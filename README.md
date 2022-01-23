# Simple blog

Jednoduchý blogový systém, založerný na python frameworku Flask.


## Závislosti

* [Flask](https://flask.palletsprojects.com/en/latest/)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [SQLAlchemy-mixins](https://github.com/absent1706/sqlalchemy-mixins)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
* [W3.css](https://www.w3schools.com/w3css/)

Kompletný zoznam závislostí je zapísaný v súbore [requirements.txt](requirements.txt).


## Spustenie projektu

Pre spustenie projektu je potrebné mať nainštalovaný [python3](https://www.python.org/downloads/), [pip](https://pypi.org/project/pip/), [virtualenv](https://pypi.org/project/virtualenv/) a git.

#### 1 Stiahnutie projektu
```shell
$ git clone https://github.com/lukasondrejka/simple-blog.git
$ cd simple-blog
```

#### 2 Vytvorenie a aktivácia virtuálneho prostrediea virtualenv a stiahnutie závislostí.
```shell
$ python -m venv .venv
$ source .venv/bin/activate
(venv)$ pip install -r requirements.txt
```

#### 3 Spustenie projektu
```shell
(venv)$ python app.py
```

