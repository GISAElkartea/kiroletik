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
