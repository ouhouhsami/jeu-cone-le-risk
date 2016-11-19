docker-machine start risks
eval "$(docker-machine env risks)"
export URL='http://'$(docker-machine ip risks)
python -mwebbrowser $URL
docker-compose up
