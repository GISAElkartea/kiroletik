Install
=======

    # Python requirements
    pip install -r requirements/base.txt

    # JS requirements
    cd kiroletik/static/
    bower install
    cd ../../

    # DB creation
    python manage.py migrate

    # Admin user creation
    python manage.py createsuperuser


Sample data
===========

    python manage.py loaddata sample_data.json


Test
====

[![Build Status](https://travis-ci.org/GISAElkartea/kiroletik.svg?branch=master)](https://travis-ci.org/GISAElkartea/kiroletik)

    pip install -r requirements/dev.txt
    python manage.py test


Run
===

    python manage.py runserver


Push to heroku
==============

    pip install -r requirements/heroku.txt
    # After setting up the heroku credentials with
    # heroku login
    git push heroku master


Required views
==============

- flatpages
- news detail
- latest news (paginated)
- latest news per sport (paginated)
    - list of competitions and seasons
- season detail
- latest match results (paginated)
