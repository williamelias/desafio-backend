docker-compose run web coverage run --source='user_auth' \
    --omit='*/migrations/*.py','*__init__.py','*/models/_*.py','*/commands/*' manage.py test  \
    --verbosity 2 

docker-compose run web coverage html