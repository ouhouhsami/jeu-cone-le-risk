#sh /src/scripts/wait.sh

cd /src
export DJANGO_SETTINGS_MODULE=<project_name>.settings
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages
uwsgi --socket :8000 --wsgi-file /src/<project_name>/wsgi.py --chdir /src/<project_name> --master --processes 4 --threads 2 --py-autoreload 3
