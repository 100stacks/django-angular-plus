# django-angular-plus

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

* Fork this repository.
* `$ git clone git@github.com:<your username>/django-angular-plus.git` **_[Uses SSH to clone]_**  
*  If using HTTPS, use: $ git clone https://github.com/site-demo/django-angular-plus.git
* `$ mkvirtualenv djangular-angular-plus`
* `$ cd django-angular-plus/`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

**_Django SECRET_KEY set from a file, so this will have to be generated if deploying this application_**