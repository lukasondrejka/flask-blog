# Flask blog

Simple blogging system written in Python using Flask framework. Application is using Mysql (mariadb) database for storing data, SQLAlchemy for ORM and WTForms for forms.

![blog](https://user-images.githubusercontent.com/20649778/171685742-5fe16c3b-f313-4d32-87df-012859a0305d.png)


## Dependencies

* [Flask](https://flask.palletsprojects.com/en/latest/)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [SQLAlchemy-mixins](https://github.com/absent1706/sqlalchemy-mixins)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
* [W3.css](https://www.w3schools.com/w3css/)

Full list of dependencies can be found in [requirements.txt](app/requirements.txt).


## Project setup

### Requirements

* Docker
* docker-compose

### Setup

```bash
docker-compose up
```

Application will be available at [localhost](http://localhost). Login credentials for [login page](http://localhost/login) are `admin@localhost` and `password`.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Home page |
| /login | GET, POST | Login |
| /logout | GET | Logout |
| /post/create | GET, POST | Create post |
| /post/{id} | GET | Post |
| /post/{id}/edit | GET, POST | Edit post |
| /post/{id}/remove | GET, POST | Delete post |
| /user/create | GET, POST | Create user |
| /user/{id} | GET | User profile |
| /user/{id}/edit | GET, POST | Edit user |
