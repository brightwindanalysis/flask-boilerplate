# flask-boilerplate

> TODO work in progress

### Documentation

* [Flask](http://flask.pocoo.org)
* [Python setup](doc/python.md)

### Setup
```
# create virtualenv
virtualenv -p $(which python3) env

# activate virtualenv
source env/bin/activate

# deactivate virtualenv
deactivate

# install requirements
pip install -r requirements.txt

# verify code
pylint app/app.py
find ./app -iname "*.py" | xargs pylint
```

### Run
```
# activate virtualenv
source env/bin/activate

# start app local
python ./app/main.py

# override config
FLASK_PORT=8080 \
  python ./app/main.py
```

### Docker
```
# build image
docker build -t brightwindanalysis/flask-boilerplate:latest .

# start temporary container
docker run \
  --rm \
  -e FLASK_PORT=8080 \
  -p 3000:8080 \
  --name flask-boilerplate \
  brightwindanalysis/flask-boilerplate:latest

# test
http :3000

# access container
docker exec -it flask-boilerplate bash

# TODO verify dockerignore skip __pycache__ and *.pyc
```
