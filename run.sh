docker-machine start risks
eval "$(docker-machine env risks)"
docker-compose run -e DJANGO_SETTINGS_MODULE=risks.settings -w /src web bash