# flask-boilerplate

> TODO

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

### Docker
```
# build image
docker build -t brightwindanalysis/flask-boilerplate:latest .

# start temporary container
docker run \
  --rm \
  -p 3000:5000 \
  --name flask-boilerplate \
  brightwindanalysis/flask-boilerplate:latest

# test
http :3000

# access container
docker exec -it flask-boilerplate bash
```
