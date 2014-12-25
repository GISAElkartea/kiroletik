Install
=======

    # Python requirements
    pip install -r requirements.txt

    # JS requirements
    cd kiroletik/static/
    bower install
    cd ../../

    # DB creation
    python manage.py migrate

    # Admin user creation
    python manage.py createsuperuser


Run
===

    python manage.py runserver


Required views
==============

- flatpages
- news detail
- latest news (paginated)
- latest news per sport (paginated)
    - list of competitions and seasons
- season detail
- latest match results (paginated)
